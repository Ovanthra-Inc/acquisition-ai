import jwt
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Optional, List
import logging

logger = logging.getLogger(__name__)

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, secret_key: str, algorithms: List[str] = ["HS256"]):
        super().__init__(app)
        self.secret_key = secret_key
        self.algorithms = algorithms

    async def dispatch(self, request: Request, call_next):
        # Skip auth for docs, openapi, and specific health checks
        if request.url.path in ["/docs", "/openapi.json", "/redoc", "/health"]:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            # We allow the request to proceed but without user context
            # Individual routes can then check for request.state.user_id
            request.state.user_id = None
            request.state.tenant_id = None
            request.state.role = None
            request.state.tier = None
            return await call_next(request)

        token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=self.algorithms)
            request.state.user_id = payload.get("user_id")
            request.state.tenant_id = payload.get("tenant_id")
            request.state.role = payload.get("role")
            request.state.tier = payload.get("tier")
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
        except Exception as e:
            logger.error(f"Auth error: {str(e)}")
            raise HTTPException(status_code=401, detail="Authentication failed")

        response = await call_next(request)
        return response

def requires_role(roles: List[str]):
    def decorator(request: Request):
        user_role = getattr(request.state, "role", None)
        if user_role not in roles:
            raise HTTPException(status_code=403, detail="Permission denied")
    return decorator

def requires_tier(tiers: List[str]):
    def decorator(request: Request):
        user_tier = getattr(request.state, "tier", None)
        if user_tier not in tiers:
            raise HTTPException(status_code=403, detail="Upgrade required to access this feature")
    return decorator

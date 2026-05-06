from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.security import verify_jwt

PUBLIC_PATHS = [
    "/docs", 
    "/openapi.json", 
    "/api/v1/auth/login/google", 
    "/api/v1/auth/callback/google",
    "/api/v1/webhooks"
]

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        # 1. Block external access to internal endpoints
        if "/internal/" in path:
            return JSONResponse(status_code=403, content={"detail": "Forbidden: Internal endpoints cannot be accessed externally"})

        # 2. Allow public paths without auth
        if any(path.startswith(p) for p in PUBLIC_PATHS):
            return await call_next(request)

        # 3. Enforce auth header
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return JSONResponse(status_code=401, content={"detail": "Missing Authentication Token"})

        parts = auth_header.split(" ")
        if len(parts) != 2 or parts[0].lower() != "bearer":
            return JSONResponse(status_code=401, content={"detail": "Invalid Authentication Header Format"})

        token = parts[1]
        try:
            payload = verify_jwt(token)
            request.state.user = payload
        except Exception:
            # Catching the HTTPException raised by verify_jwt and converting to JSONResponse
            return JSONResponse(status_code=401, content={"detail": "Invalid or Expired Token"})
                
        return await call_next(request)

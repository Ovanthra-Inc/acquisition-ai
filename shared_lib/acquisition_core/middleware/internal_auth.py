from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import hmac
import hashlib

def generate_internal_signature(internal_token: str, user_id: str, tenant_id: str, service_name: str) -> str:
    data = f"{user_id}:{tenant_id}:{service_name}"
    return hmac.new(
        internal_token.encode(),
        data.encode(),
        hashlib.sha256
    ).hexdigest()

def verify_internal_signature(internal_token: str, user_id: str, tenant_id: str, service_name: str, signature: str):
    expected = generate_internal_signature(internal_token, user_id, tenant_id, service_name)
    return hmac.compare_digest(expected, signature)

class InternalAuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, internal_token: str, exclude_paths: list[str] = None):
        super().__init__(app)
        self.internal_token = internal_token
        self.exclude_paths = exclude_paths or ["/docs", "/openapi.json", "/redoc", "/", "/api/v1/auth/login/google", "/api/v1/auth/callback/google", "/api/v1/webhooks"]

    async def dispatch(self, request: Request, call_next):
        if any(request.url.path.startswith(path) for path in self.exclude_paths) or request.url.path in self.exclude_paths:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header or auth_header != f"Bearer {self.internal_token}":
            from fastapi.responses import JSONResponse
            return JSONResponse(status_code=401, content={"detail": "Missing or invalid internal token"})

        signature = request.headers.get("X-Request-Signature")
        user_id = request.headers.get("X-User-Id", "")
        tenant_id = request.headers.get("X-Tenant-Id", "")
        service_name = request.headers.get("X-Service-Name", "")

        # If it's not a service call and has no user ID, it's invalid
        if not user_id and not service_name:
            from fastapi.responses import JSONResponse
            return JSONResponse(status_code=403, content={"detail": "Missing user or service context"})

        if not signature or not verify_internal_signature(self.internal_token, user_id, tenant_id, service_name, signature):
            from fastapi.responses import JSONResponse
            return JSONResponse(status_code=403, content={"detail": "Invalid request signature"})

        request.state.user_id = user_id
        request.state.tenant_id = tenant_id
        request.state.service_name = service_name

        return await call_next(request)

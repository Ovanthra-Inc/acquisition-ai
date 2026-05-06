from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from app.core.rate_limiter import check_rate_limit

class RateLimitMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        user = getattr(request.state, "user", None)

        if user and "user_id" in user:
            await check_rate_limit(user["user_id"], request.url.path)

        return await call_next(request)

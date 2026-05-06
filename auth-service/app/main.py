from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from app.core.config import settings
from app.api.v1.router import api_router
from acquisition_core.middleware.internal_auth import InternalAuthMiddleware

app = FastAPI(title=settings.PROJECT_NAME)

# Authlib requires session middleware
app.add_middleware(SessionMiddleware, secret_key=settings.JWT_SECRET)

# Add internal auth middleware (except for google oauth callbacks)
app.add_middleware(
    InternalAuthMiddleware, 
    internal_token=settings.INTERNAL_SERVICE_TOKEN,
    exclude_paths=["/docs", "/openapi.json", "/api/v1/auth/login/google", "/api/v1/auth/callback/google", "/"]
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}

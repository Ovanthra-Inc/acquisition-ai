from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.router import api_router
from acquisition_core.middleware.internal_auth import InternalAuthMiddleware

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    InternalAuthMiddleware,
    internal_token=settings.INTERNAL_SERVICE_TOKEN,
    exclude_paths=["/docs", "/openapi.json", "/"]
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}

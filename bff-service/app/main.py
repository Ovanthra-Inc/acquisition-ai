from fastapi import FastAPI
from app.api.v1.endpoints import dashboard
from app.core.config import settings

app = FastAPI(title="BFF Service")

app.include_router(dashboard.router, prefix="/api/v1/dashboard", tags=["dashboard"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}

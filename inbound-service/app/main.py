from fastapi import FastAPI
from app.api.v1.endpoints import inbox
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(inbox.router, prefix=settings.API_V1_STR + "/inbound", tags=["Inbound"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}

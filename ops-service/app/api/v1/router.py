from fastapi import APIRouter
from app.api.v1.endpoints import analytics

api_router = APIRouter()
api_router.include_router(analytics.router, prefix="/analytics", tags=["analytics"])

# Stubs for other merged services to maintain API compatibility
@api_router.get("/system")
def get_system():
    return {"message": "System observability endpoint (merged)"}

@api_router.get("/audit")
def get_audit():
    return {"message": "Audit endpoint (merged)"}

@api_router.get("/api-keys")
def get_api_keys():
    return {"message": "Platform API-Keys endpoint (merged)"}

@api_router.get("/limits")
def get_limits():
    return {"message": "Rate limits endpoint (merged)"}

@api_router.get("/proxy")
def get_proxy():
    return {"message": "Proxy endpoint (merged)"}

from fastapi import APIRouter
from app.api.v1.endpoints import auth, profile, organization

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(profile.router, prefix="/users", tags=["users"])
api_router.include_router(organization.router, prefix="/organizations", tags=["organizations"])

# Stubs for other merged services to maintain API compatibility
@api_router.get("/roles")
def get_roles():
    return {"message": "RBAC roles endpoint (merged)"}

@api_router.get("/policies")
def get_policies():
    return {"message": "Policies endpoint (merged)"}

@api_router.get("/billing")
def get_billing():
    return {"message": "Billing endpoint (merged)"}

@api_router.get("/security")
def get_security():
    return {"message": "Security endpoint (merged)"}

from fastapi import APIRouter
from app.api.v1.endpoints import organization

api_router = APIRouter()
api_router.include_router(organization.router, prefix="/organizations", tags=["organizations"])

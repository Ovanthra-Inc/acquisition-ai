from fastapi import APIRouter
from app.api.v1.endpoints import optimization

api_router = APIRouter()
api_router.include_router(optimization.router, prefix="/optimization", tags=["optimization"])

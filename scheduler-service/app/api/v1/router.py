from fastapi import APIRouter
from app.api.v1.endpoints import scheduler

api_router = APIRouter()
api_router.include_router(scheduler.router, prefix="/scheduler", tags=["scheduler"])

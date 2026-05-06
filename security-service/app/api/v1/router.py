from fastapi import APIRouter
from app.api.v1.endpoints import limits, events

api_router = APIRouter()

api_router.include_router(limits.router, prefix="/limits", tags=["limits"])
api_router.include_router(events.router, prefix="/events", tags=["events"])

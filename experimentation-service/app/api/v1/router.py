from fastapi import APIRouter
from app.api.v1.endpoints import experiment

api_router = APIRouter()
api_router.include_router(experiment.router, prefix="/experiment", tags=["experiment"])

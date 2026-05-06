from fastapi import APIRouter
from app.api.v1.endpoints import enrichment

api_router = APIRouter()
api_router.include_router(enrichment.router, prefix="/enrichment", tags=["enrichment"])

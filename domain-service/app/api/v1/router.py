from fastapi import APIRouter
from app.api.v1.endpoints import domains, sources, signals

api_router = APIRouter()
api_router.include_router(domains.router, prefix="/domains", tags=["domains"])
api_router.include_router(sources.router, prefix="/sources", tags=["sources"])
api_router.include_router(signals.router, prefix="/signals", tags=["signals"])

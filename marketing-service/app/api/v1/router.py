from fastapi import APIRouter
from app.api.v1.endpoints import lead, campaigns, pipeline, enrichment, domains

api_router = APIRouter()
api_router.include_router(lead.router, prefix="/leads", tags=["leads"])
api_router.include_router(campaigns.router, prefix="/campaigns", tags=["campaigns"])
api_router.include_router(pipeline.router, prefix="/pipeline", tags=["pipeline"])
api_router.include_router(enrichment.router, prefix="/enrichment", tags=["enrichment"])
api_router.include_router(domains.router, prefix="/domains", tags=["domains"])

from fastapi import APIRouter, Request
from app.schemas.enrichment import EnrichRequest, EnrichResponse, ScoreRequest, ScoreResponse
from app.services.enrichment_service import EnrichmentService

router = APIRouter()
service = EnrichmentService()

@router.post("/enrich", response_model=EnrichResponse)
def enrich_lead(request: Request, data: EnrichRequest):
    return service.enrich(data.dict())

@router.post("/score", response_model=ScoreResponse)
def score_lead(request: Request, data: ScoreRequest):
    return service.score(data.dict())

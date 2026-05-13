from fastapi import APIRouter, Depends, Request, HTTPException
from app.services.enrichment_service import EnrichmentService
from typing import Dict, Any

router = APIRouter()
service = EnrichmentService()

@router.post("/crawl")
def crawl_website(url: str):
    return {"text": service.crawl(url)}

@router.post("/enrich")
def enrich_lead(data: Dict[str, Any]):
    return service.enrich(data)

@router.post("/score")
def score_lead(data: Dict[str, Any]):
    return service.score(data)

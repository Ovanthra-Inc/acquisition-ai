from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.domain_service import DomainService
from typing import List

router = APIRouter()
domain_service = DomainService()

class SearchRequest(BaseModel):
    domain: str
    keyword: str

class MergeRequest(BaseModel):
    lead_id: str
    domains: List[str]

@router.get("/")
async def list_domains():
    return {"domains": ["website", "hiring", "local"]}

@router.post("/search")
async def search_domain(request: SearchRequest):
    try:
        results = domain_service.search(request.domain, request.keyword)
        return {"results": results}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/merge")
async def merge_lead_data(request: MergeRequest):
    """Agent tool calls: POST /api/v1/domains/merge"""
    # In production: cross-reference lead data across domain adapters
    merged = {}
    for domain in request.domains:
        try:
            results = domain_service.search(domain, "")
            merged[domain] = {"source": domain, "records": len(results)}
        except ValueError:
            merged[domain] = {"source": domain, "records": 0, "error": "adapter not found"}
    
    return {
        "lead_id": request.lead_id,
        "status": "merged",
        "domains_processed": list(merged.keys()),
        "summary": merged
    }


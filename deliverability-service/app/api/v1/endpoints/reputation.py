from fastapi import APIRouter
from app.services.reputation_service import ReputationService
from pydantic import BaseModel

router = APIRouter()
service = ReputationService()

class MetricsInput(BaseModel):
    domain: str
    bounce_rate: float = 0.0
    spam_rate: float = 0.0

@router.get("/")
async def list_reputations():
    return {"status": "ok", "domains": []}

@router.get("/{domain}")
async def get_domain_reputation(domain: str):
    """Agent tool calls: GET /api/v1/deliverability/reputation/{domain}"""
    score = service.calculate_score({"bounce_rate": 0.0, "spam_rate": 0.0})
    status = "healthy" if score >= 80 else "warning" if score >= 50 else "critical"
    return {"domain": domain, "score": score, "status": status}

@router.post("/calculate")
async def calculate_reputation(metrics: MetricsInput):
    score = service.calculate_score({
        "bounce_rate": metrics.bounce_rate,
        "spam_rate": metrics.spam_rate
    })
    status = "healthy" if score >= 80 else "warning" if score >= 50 else "critical"
    return {"domain": metrics.domain, "score": score, "status": status}

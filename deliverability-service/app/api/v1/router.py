from fastapi import APIRouter
from app.api.v1.endpoints import reputation, warmup

api_router = APIRouter()

api_router.include_router(reputation.router, prefix="/deliverability/reputation", tags=["reputation"])
api_router.include_router(warmup.router, prefix="/deliverability/warmup", tags=["warmup"])

# Abuse check endpoint (inline since it's simple)
from pydantic import BaseModel

class AbuseCheckRequest(BaseModel):
    user_id: str
    action: str

@api_router.post("/deliverability/abuse-check", tags=["abuse"])
async def check_abuse(request: AbuseCheckRequest):
    """Agent tool calls: POST /api/v1/deliverability/abuse-check"""
    # In production: check Redis for velocity patterns, IP reputation, etc.
    return {"user_id": request.user_id, "action": request.action, "risk": "low"}

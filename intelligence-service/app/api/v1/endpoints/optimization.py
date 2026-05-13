from fastapi import APIRouter
from app.services.optimization_service import OptimizationService
from pydantic import BaseModel

router = APIRouter()
service = OptimizationService()

class OptimizationRequest(BaseModel):
    reply_rate: float = 0.0
    open_rate: float = 0.0

@router.post("/analyze")
async def analyze_campaign(request: OptimizationRequest):
    return service.optimize_campaign(request.dict())

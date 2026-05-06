from fastapi import APIRouter
from app.services.warmup_service import WarmupService
from pydantic import BaseModel

router = APIRouter()
service = WarmupService()

class WarmupRequest(BaseModel):
    domain: str

@router.post("/")
async def start_warmup(request: WarmupRequest):
    result = service.schedule_warmup(request.domain)
    return result

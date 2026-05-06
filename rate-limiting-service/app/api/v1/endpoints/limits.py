from fastapi import APIRouter, Depends, HTTPException
from app.services.rate_limit_service import RateLimitService

router = APIRouter()
rate_limit_service = RateLimitService()

@router.get("/")
async def get_limits():
    return {"message": "Rate limits status"}

@router.post("/check")
async def check_limit(user_id: str, limit_type: str, limit: int):
    allowed = await rate_limit_service.allow_request(user_id, limit_type, limit)
    if not allowed:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    return {"status": "allowed"}

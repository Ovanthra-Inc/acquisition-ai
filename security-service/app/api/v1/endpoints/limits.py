from fastapi import APIRouter, HTTPException
from app.services.rate_limiter import RateLimiter
from pydantic import BaseModel

router = APIRouter()
limiter = RateLimiter()

class LimitCheckRequest(BaseModel):
    user_id: str
    limit: int

@router.post("/")
async def check_limit(request: LimitCheckRequest):
    allowed = limiter.allow_request(request.user_id, request.limit)
    if not allowed:
        raise HTTPException(status_code=429, detail="Too Many Requests")
    return {"status": "allowed"}

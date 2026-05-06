import redis.asyncio as redis
from fastapi import HTTPException
from app.core.config import settings

r = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)

async def check_rate_limit(user_id: str, path: str = ""):
    limit = 10 if "/api/v1/enrichment" in path else 100
    
    # Specific key for enrichment to avoid locking out global API access
    prefix = "enrich" if "/api/v1/enrichment" in path else "global"
    key = f"rate:{prefix}:{user_id}"
    
    async with r.pipeline(transaction=True) as pipe:
        pipe.get(key)
        pipe.incr(key)
        pipe.expire(key, 60)
        results = await pipe.execute()
        
    count = results[0]
    if count and int(count) >= limit:
        raise HTTPException(status_code=429, detail=f"Rate limit exceeded for {prefix}")

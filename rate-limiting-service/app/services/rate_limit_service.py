import redis.asyncio as redis
from app.core.config import settings

class RateLimitService:
    def __init__(self):
        self.redis = redis.from_url(settings.REDIS_URL)

    async def allow_request(self, key: str, limit_type: str, limit: int) -> bool:
        redis_key = f"rate_limit:{limit_type}:{key}"
        current = await self.redis.get(redis_key)
        
        if current and int(current) >= limit:
            return False
            
        await self.redis.incr(redis_key)
        # Set expiration if it's a new key
        if not current:
            await self.redis.expire(redis_key, 60) # Default 1 minute window
            
        return True

import redis
from app.core.config import settings

class RateLimiter:
    def __init__(self):
        # We assume redis is available at REDIS_URL
        self.redis_client = redis.from_url(settings.REDIS_URL)

    def allow_request(self, user_id: str, limit: int) -> bool:
        key = f"rate_limit:{user_id}"
        current = self.redis_client.get(key)

        if current and int(current) >= limit:
            return False

        self.redis_client.incr(key)
        # Set expiration to 1 hour if not set
        if self.redis_client.ttl(key) == -1:
            self.redis_client.expire(key, 3600)
            
        return True

from sqlalchemy.orm import Session
from app.repository.event_repo import EventRepository
from uuid import UUID
import redis
import json
import os

redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")
redis_client = redis.Redis.from_url(redis_url, decode_responses=True)

class AnalyticsService:
    def __init__(self):
        self.repo = EventRepository()

    def track_event(self, db: Session, user_id: UUID, data: dict):
        return self.repo.create(db, user_id, data)

    def get_overview(self, db: Session, user_id: UUID):
        cache_key = f"analytics:overview:{user_id}"
        cached = redis_client.get(cache_key)
        if cached:
            return json.loads(cached)
            
        sent_events = self.repo.get_events_by_type(db, user_id, "email_sent")
        reply_events = self.repo.get_events_by_type(db, user_id, "reply_received")
        
        total_sent = len(sent_events)
        total_replies = len(reply_events)
        
        conversion = 0.0
        if total_sent > 0:
            conversion = (total_replies / total_sent) * 100
            
        result = {
            "total_emails_sent": total_sent,
            "total_replies": total_replies,
            "conversion_rate": conversion
        }
        
        redis_client.setex(cache_key, 300, json.dumps(result)) # 5 min TTL
        return result

from pydantic import BaseModel
from typing import Dict, Any, Optional
from uuid import UUID
from datetime import datetime

class EventCreate(BaseModel):
    event_type: str
    metadata: Dict[str, Any]
    user_id: Optional[UUID] = None
    tenant_id: Optional[UUID] = None

class EventResponse(BaseModel):
    id: UUID
    event_type: str
    metadata: Dict[str, Any]
    created_at: datetime

    class Config:
        from_attributes = True

class AnalyticsOverview(BaseModel):
    total_events: int
    events_by_type: Dict[str, int]
    daily_active_users: int

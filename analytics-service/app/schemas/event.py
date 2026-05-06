from pydantic import BaseModel
from typing import Dict, Any
from uuid import UUID
from datetime import datetime

class EventCreate(BaseModel):
    type: str
    metadata: Dict[str, Any]

class EventResponse(BaseModel):
    id: UUID
    user_id: UUID
    type: str
    metadata: Dict[str, Any]
    created_at: datetime
    
    class Config:
        orm_mode = True

class AnalyticsOverview(BaseModel):
    total_emails_sent: int
    total_replies: int
    conversion_rate: float

from pydantic import BaseModel
from typing import Optional, Dict, Any
from uuid import UUID
from datetime import datetime

class NotificationCreate(BaseModel):
    user_id: UUID
    title: str
    message: str
    type: str = "info"
    metadata: Optional[Dict[str, Any]] = None

class NotificationResponse(BaseModel):
    id: UUID
    title: str
    message: str
    type: str
    read: bool
    created_at: datetime

    class Config:
        from_attributes = True

class ReadRequest(BaseModel):
    notification_ids: list[UUID]

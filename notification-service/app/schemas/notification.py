from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class NotificationCreate(BaseModel):
    user_id: UUID
    message: str
    type: str

class NotificationResponse(BaseModel):
    id: UUID
    user_id: UUID
    message: str
    type: str
    is_read: bool
    created_at: datetime
    
    class Config:
        orm_mode = True

class ReadRequest(BaseModel):
    notification_id: UUID

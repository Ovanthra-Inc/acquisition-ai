from pydantic import BaseModel, EmailStr
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class SendEmailRequest(BaseModel):
    recipient: str
    subject: str
    body: str
    lead_id: Optional[UUID] = None
    campaign_id: Optional[UUID] = None

class EmailLogResponse(BaseModel):
    id: UUID
    recipient: str
    subject: str
    status: str
    sent_at: datetime

    class Config:
        from_attributes = True

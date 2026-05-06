from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class SendEmailRequest(BaseModel):
    campaign_id: UUID
    lead_id: UUID
    to_email: str
    subject: str
    body: str

class EmailLogResponse(BaseModel):
    id: UUID
    campaign_id: UUID
    lead_id: UUID
    subject: str
    status: str
    sent_at: Optional[datetime]
    
    class Config:
        orm_mode = True

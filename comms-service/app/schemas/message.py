from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class MessageCreate(BaseModel):
    conversation_id: UUID
    sender: str
    body: str

class MessageResponse(BaseModel):
    id: UUID
    conversation_id: UUID
    sender: str
    body: str
    classified_as: str
    created_at: datetime
    
    class Config:
        orm_mode = True

class ClassifyRequest(BaseModel):
    message_text: str

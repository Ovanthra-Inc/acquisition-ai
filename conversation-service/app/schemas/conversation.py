from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from datetime import datetime
from app.schemas.message import MessageResponse

class ConversationCreate(BaseModel):
    lead_id: UUID
    thread_id: Optional[str]

class ConversationResponse(BaseModel):
    id: UUID
    user_id: UUID
    lead_id: UUID
    thread_id: Optional[str]
    created_at: datetime
    messages: List[MessageResponse] = []
    
    class Config:
        orm_mode = True

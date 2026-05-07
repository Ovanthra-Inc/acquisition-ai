from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

from typing import Optional

class LeadCreate(BaseModel):
    company_name: str
    website: Optional[str] = None
    email: Optional[str] = None

class LeadResponse(BaseModel):
    id: UUID
    user_id: UUID
    company_name: str
    website: Optional[str] = None
    email: Optional[str] = None
    score: Optional[int] = 0
    status: str
    created_at: datetime
    
    class Config:
        orm_mode = True

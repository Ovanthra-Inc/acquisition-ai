from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class LeadCreate(BaseModel):
    company_name: str
    website: str
    email: str

class LeadResponse(BaseModel):
    id: UUID
    user_id: UUID
    company_name: str
    website: str
    email: str
    score: int
    status: str
    created_at: datetime
    
    class Config:
        orm_mode = True

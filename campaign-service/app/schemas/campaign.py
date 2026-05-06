from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime import datetime

class CampaignCreate(BaseModel):
    name: str

class CampaignResponse(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    status: str
    created_at: datetime
    
    class Config:
        orm_mode = True

class AddLeadsRequest(BaseModel):
    lead_ids: List[UUID]

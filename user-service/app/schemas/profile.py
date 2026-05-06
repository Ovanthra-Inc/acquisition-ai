from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class UserProfileCreateUpdate(BaseModel):
    offer: str
    target_audience: str
    problem: str
    usp: str
    outcome: str

class UserProfileResponse(UserProfileCreateUpdate):
    id: UUID
    user_id: UUID

    class Config:
        orm_mode = True

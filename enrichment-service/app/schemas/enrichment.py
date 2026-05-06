from pydantic import BaseModel
from typing import Dict, Any

class EnrichRequest(BaseModel):
    company_name: str
    website: str

class EnrichResponse(BaseModel):
    industry: str
    description: str
    pain_points: str

class ScoreRequest(BaseModel):
    lead_data: Dict[str, Any]

class ScoreResponse(BaseModel):
    score: int

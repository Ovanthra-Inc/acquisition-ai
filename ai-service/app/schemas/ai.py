from pydantic import BaseModel
from typing import Dict, Any

class GenerateEmailRequest(BaseModel):
    lead_data: Dict[str, Any]
    user_profile: Dict[str, Any]
    
class GenerateEmailResponse(BaseModel):
    subject: str
    body: str

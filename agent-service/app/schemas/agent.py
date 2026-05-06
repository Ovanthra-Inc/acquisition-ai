from pydantic import BaseModel
from typing import Optional

class AgentRunRequest(BaseModel):
    goal: str
    approved_to_send: bool = False  # Human-in-the-loop gate for email dispatch
    
class AgentApproveRequest(BaseModel):
    task_id: str
    approved: bool = True
    
class AgentRunResponse(BaseModel):
    task_id: Optional[str] = None
    message: str
    status: str
    action_required: Optional[str] = None

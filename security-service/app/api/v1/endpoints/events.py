from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class EventReportRequest(BaseModel):
    user_id: str
    event_type: str
    severity: str
    metadata: dict

@router.get("/")
async def list_events():
    return {"events": []}

@router.post("/report")
async def report_event(request: EventReportRequest):
    return {"status": "reported", "event_type": request.event_type}

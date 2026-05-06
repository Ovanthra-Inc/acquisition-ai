from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_signals():
    return {"signals": ["hiring_engineer", "funding_round", "new_launch"]}

@router.get("/{lead_id}")
async def get_lead_signals(lead_id: str):
    return {"lead_id": lead_id, "signals": []}

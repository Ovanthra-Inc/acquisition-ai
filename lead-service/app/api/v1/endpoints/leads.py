from fastapi import APIRouter, Depends, Request
from app.schemas.lead import LeadCreate, LeadResponse
from app.services.lead_service import LeadService
from app.db.session import get_db
from sqlalchemy.orm import Session
from uuid import UUID

router = APIRouter()
service = LeadService()

@router.post("/", response_model=LeadResponse)
def create_lead(request: Request, data: LeadCreate, db: Session = Depends(get_db)):
    user_id = request.state.user_id
    lead_data = data.dict()
    lead_data["user_id"] = UUID(user_id)
    return service.create_lead(db, lead_data)

@router.get("/", response_model=list[LeadResponse])
def list_leads(request: Request, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    return service.list_leads(db, user_id)

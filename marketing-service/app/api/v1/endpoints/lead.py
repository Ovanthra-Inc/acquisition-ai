from fastapi import APIRouter, Depends, Request
from app.schemas.lead import LeadCreate, LeadResponse
from app.services.lead_service import LeadService
from app.db.session import get_db
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

router = APIRouter()
service = LeadService()

@router.post("/", response_model=LeadResponse)
def create_lead(request: Request, data: LeadCreate, db: Session = Depends(get_db)):
    user_id = request.headers.get("X-User-Id")
    if not user_id:
        from fastapi import HTTPException
        raise HTTPException(status_code=401, detail="X-User-Id missing")
    
    lead_data = data.model_dump()
    lead_data["user_id"] = UUID(user_id)
    return service.create_lead(db, lead_data)

@router.get("/", response_model=List[LeadResponse])
def list_leads(request: Request, db: Session = Depends(get_db)):
    user_id_str = request.headers.get("X-User-Id")
    if not user_id_str:
        from fastapi import HTTPException
        raise HTTPException(status_code=401, detail="X-User-Id missing")
    
    user_id = UUID(user_id_str)
    return service.list_leads(db, user_id)

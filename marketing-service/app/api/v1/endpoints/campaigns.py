from fastapi import APIRouter, Depends, Request, HTTPException
from app.schemas.campaign import CampaignCreate, CampaignResponse, AddLeadsRequest
from app.services.campaign_service import CampaignService
from app.db.session import get_db
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

router = APIRouter()
service = CampaignService()

@router.post("/", response_model=CampaignResponse)
def create_campaign(request: Request, data: CampaignCreate, db: Session = Depends(get_db)):
    user_id_str = request.headers.get("X-User-Id")
    if not user_id_str:
        raise HTTPException(status_code=401, detail="X-User-Id missing")
    
    user_id = UUID(user_id_str)
    return service.create(db, user_id, data.name)

@router.get("/", response_model=List[CampaignResponse])
def list_campaigns(request: Request, db: Session = Depends(get_db)):
    user_id_str = request.headers.get("X-User-Id")
    if not user_id_str:
        raise HTTPException(status_code=401, detail="X-User-Id missing")
    
    user_id = UUID(user_id_str)
    return service.list_all(db, user_id)

@router.post("/{campaign_id}/add-leads")
def add_leads(request: Request, campaign_id: UUID, data: AddLeadsRequest, db: Session = Depends(get_db)):
    user_id_str = request.headers.get("X-User-Id")
    if not user_id_str:
        raise HTTPException(status_code=401, detail="X-User-Id missing")
    
    # In a real app, we should verify the user owns the campaign
    return service.attach_leads(db, campaign_id, [l.model_dump() for l in data.leads])

@router.post("/{campaign_id}/send")
def send_campaign(request: Request, campaign_id: UUID, db: Session = Depends(get_db)):
    user_id_str = request.headers.get("X-User-Id")
    if not user_id_str:
        raise HTTPException(status_code=401, detail="X-User-Id missing")
    
    user_id = UUID(user_id_str)
    return service.send_campaign(db, campaign_id, user_id)

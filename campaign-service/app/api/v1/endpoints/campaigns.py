from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from uuid import UUID
from app.db.session import get_db
from app.schemas.campaign import CampaignCreate, CampaignResponse, AddLeadsRequest
from app.services.campaign_service import CampaignService

router = APIRouter()
service = CampaignService()

@router.post("/", response_model=CampaignResponse)
def create_campaign(request: Request, data: CampaignCreate, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    return service.create(db, user_id, data.name)

@router.get("/", response_model=list[CampaignResponse])
def get_campaigns(request: Request, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    return service.list_all(db, user_id)

@router.post("/{campaign_id}/add-leads")
def add_leads(request: Request, campaign_id: UUID, data: AddLeadsRequest, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    return service.attach_leads(db, campaign_id, data.lead_ids)

@router.post("/{campaign_id}/send")
def send_campaign(request: Request, campaign_id: UUID, db: Session = Depends(get_db)):
    return service.send_campaign(db, campaign_id)

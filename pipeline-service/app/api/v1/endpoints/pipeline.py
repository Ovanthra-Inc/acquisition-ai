from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.services.pipeline_service import PipelineService
from pydantic import BaseModel
from uuid import UUID
from typing import Optional

engine = create_engine(settings.DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()
service = PipelineService()

class DealCreate(BaseModel):
    lead_id: str
    campaign_id: Optional[str] = None
    value: float = 0.0

class DealStageUpdate(BaseModel):
    new_stage_id: str

@router.get("/stages")
def get_pipeline_stages(request: Request, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    stages = service.get_stages(db, user_id)
    return {"stages": [{"id": str(s.id), "name": s.name, "order": s.order} for s in stages]}

@router.post("/deals")
def create_deal(request: Request, data: DealCreate, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    lead_id = UUID(data.lead_id)
    campaign_id = UUID(data.campaign_id) if data.campaign_id else None
    
    deal = service.create_deal(db, user_id, lead_id, campaign_id, data.value)
    return {"id": str(deal.id), "status": "created"}

@router.get("/deals")
def get_deals(request: Request, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    deals = service.get_deals(db, user_id)
    return {"deals": [{"id": str(d.id), "lead_id": str(d.lead_id), "stage_id": str(d.stage_id), "value": d.value} for d in deals]}

@router.patch("/deals/{deal_id}/stage")
def update_deal_stage(request: Request, deal_id: str, data: DealStageUpdate, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    d_id = UUID(deal_id)
    stage_id = UUID(data.new_stage_id)
    
    deal = service.update_deal_stage(db, d_id, user_id, stage_id)
    if not deal:
        raise HTTPException(status_code=404, detail="Deal not found")
        
    return {"id": str(deal.id), "status": "updated", "stage_id": str(deal.stage_id)}

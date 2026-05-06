from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from uuid import UUID
from app.db.session import get_db
from app.schemas.event import EventCreate, EventResponse, AnalyticsOverview
from app.services.analytics_service import AnalyticsService

router = APIRouter()
service = AnalyticsService()

@router.post("/track", response_model=EventResponse)
def track_event(request: Request, data: EventCreate, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    return service.track_event(db, user_id, data.dict())

@router.get("/overview", response_model=AnalyticsOverview)
def get_overview(request: Request, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    return service.get_overview(db, user_id)

@router.get("/funnel")
def get_funnel_analysis(request: Request, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    return {"funnel": "Funnel analysis data"}

@router.get("/trends")
def get_trend_analysis(request: Request, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    return {"trends": "Trend analysis data"}

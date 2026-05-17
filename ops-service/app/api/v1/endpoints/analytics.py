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

@router.get("/campaign/{campaign_id}/ab-test")
def get_campaign_ab_test(campaign_id: str, request: Request, db: Session = Depends(get_db)):
    """Returns comparative metrics for A/B variants in a campaign."""
    # Mock aggregation of event data
    return {
        "campaign_id": campaign_id,
        "variants": [
            {
                "name": "Variant A (Direct Style)",
                "opens": 145,
                "clicks": 23,
                "replies": 12,
                "open_rate": 0.58,
                "reply_rate": 0.08
            },
            {
                "name": "Variant B (Curiosity Gap)",
                "opens": 198,
                "clicks": 45,
                "replies": 8,
                "open_rate": 0.79,
                "reply_rate": 0.04
            }
        ],
        "winner": "Variant B",
        "metric_focus": "open_rate"
    }

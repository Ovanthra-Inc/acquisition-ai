from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.learning import StylePattern
from sqlalchemy import func
from typing import List, Dict

router = APIRouter()

@router.get("/patterns/stats")
def get_pattern_stats(request: Request, db: Session = Depends(get_db)):
    """Aggregates success rates for different style patterns."""
    tenant_id = request.headers.get("X-Tenant-Id")
    
    # In a real app, we would calculate conversion rates based on campaign outcomes.
    # For now, we'll return aggregated counts from our learning vault.
    stats = db.query(
        StylePattern.pattern_type,
        func.count(StylePattern.id).label("count"),
        func.sum(StylePattern.success_count).label("total_success")
    ).filter(StylePattern.tenant_id == tenant_id).group_by(StylePattern.pattern_type).all()
    
    return [
        {
            "type": s.pattern_type,
            "count": s.count,
            "avg_success": s.total_success / s.count if s.count > 0 else 0
        } for s in stats
    ]

@router.get("/patterns/top")
def get_top_patterns(request: Request, db: Session = Depends(get_db)):
    """Returns the top performing patterns for the tenant."""
    tenant_id = request.headers.get("X-Tenant-Id")
    return db.query(StylePattern).filter(StylePattern.tenant_id == tenant_id).order_by(StylePattern.success_count.desc()).limit(5).all()

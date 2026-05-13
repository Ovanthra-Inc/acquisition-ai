from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.db.base import Base

class OptimizationInsight(Base):
    __tablename__ = "optimization_insights"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), index=True)
    insight_type = Column(String) # message, targeting, timing
    recommendation = Column(String)
    confidence = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)

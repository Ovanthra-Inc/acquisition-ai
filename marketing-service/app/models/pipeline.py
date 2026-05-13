from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.db.base import Base

class PipelineStage(Base):
    __tablename__ = "pipeline_stages"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), index=True)
    name = Column(String)
    order = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class Deal(Base):
    __tablename__ = "deals"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), index=True)
    lead_id = Column(UUID(as_uuid=True), index=True)
    campaign_id = Column(UUID(as_uuid=True), nullable=True)
    stage_id = Column(UUID(as_uuid=True), ForeignKey("pipeline_stages.id"))
    value = Column(Float, default=0.0)
    status = Column(String, default="open") # open, won, lost
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

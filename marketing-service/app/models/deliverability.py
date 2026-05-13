from sqlalchemy import Column, String, Float, Integer, DateTime, JSON, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.db.base import Base

class DomainReputation(Base):
    __tablename__ = "domain_reputation"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    domain = Column(String, unique=True, index=True)
    reputation_score = Column(Float, default=100.0)
    warmup_status = Column(String, default="inactive")
    daily_limit = Column(Integer, default=50)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class WarmupJob(Base):
    __tablename__ = "warmup_jobs"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    domain = Column(String, index=True)
    status = Column(String, default="running")
    emails_sent = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

class EmailEvent(Base):
    __tablename__ = "email_events"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    campaign_id = Column(UUID(as_uuid=True), index=True)
    lead_id = Column(UUID(as_uuid=True), index=True)
    event_type = Column(String) # bounce, spam, delivery, reply
    provider_response = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

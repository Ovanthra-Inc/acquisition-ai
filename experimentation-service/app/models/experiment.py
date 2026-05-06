from sqlalchemy import Column, String, JSON, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.db.base import Base

class Experiment(Base):
    __tablename__ = "experiments"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), index=True)
    campaign_id = Column(UUID(as_uuid=True), index=True)
    experiment_type = Column(String) # ab_test, sequence_test
    status = Column(String, default="running")
    created_at = Column(DateTime, default=datetime.utcnow)

class ExperimentVariant(Base):
    __tablename__ = "experiment_variants"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    experiment_id = Column(UUID(as_uuid=True), ForeignKey("experiments.id"))
    variant_name = Column(String)
    configuration = Column(JSON)

from sqlalchemy import Column, String, JSON, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.db.base import Base

class Policy(Base):
    __tablename__ = "policies"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), index=True)
    policy_type = Column(String) # sending_limit, ai_safety, compliance
    configuration = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

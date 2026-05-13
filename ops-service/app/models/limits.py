from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.db.base import Base

class RateLimit(Base):
    __tablename__ = "rate_limits"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), index=True)
    limit_type = Column(String)
    current_usage = Column(Integer, default=0)
    reset_at = Column(DateTime)

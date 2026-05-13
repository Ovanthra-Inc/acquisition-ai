from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid
import datetime
from app.db.base import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    type = Column(String, nullable=False) # e.g., 'email_sent', 'email_opened', 'reply_received'
    payload = Column(JSONB, default=dict)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.db.base_class import Base
import enum

class ReplyCategory(str, enum.Enum):
    INTERESTED = "INTERESTED"
    INFO_REQUEST = "INFO_REQUEST"
    NOT_INTERESTED = "NOT_INTERESTED"
    OUT_OF_OFFICE = "OUT_OF_OFFICE"
    OTHER = "OTHER"

class InboxReply(Base):
    __tablename__ = "inbox_replies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lead_id = Column(UUID(as_uuid=True), nullable=False) # Reference to marketing-service lead
    tenant_id = Column(UUID(as_uuid=True), nullable=False)
    
    subject = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    category = Column(Enum(ReplyCategory), default=ReplyCategory.OTHER)
    reason = Column(Text)
    suggested_next_step = Column(Text)
    
    received_at = Column(DateTime, default=datetime.utcnow)
    processed_at = Column(DateTime)
    
    status = Column(String, default="new") # new, read, responded, archived

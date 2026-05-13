from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime
from sqlalchemy import DateTime
from app.db.base import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    company_name = Column(String)
    website = Column(String)
    email = Column(String)
    industry = Column(String, nullable=True)
    description = Column(String, nullable=True)
    pain_points = Column(String, nullable=True)
    score = Column(Integer, default=0)
    status = Column(String, default='new')
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

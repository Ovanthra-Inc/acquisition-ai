from sqlalchemy import Column, String, DateTime, func, JSON, ForeignKey, Float, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base

class Domain(Base):
    __tablename__ = "domains"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

class LeadSource(Base):
    __tablename__ = "lead_sources"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lead_id = Column(UUID(as_uuid=True), nullable=False)
    source_type = Column(String, nullable=False)
    source_url = Column(String, nullable=True)
    metadata = Column(JSON, nullable=True)

class LeadSignal(Base):
    __tablename__ = "lead_signals"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lead_id = Column(UUID(as_uuid=True), nullable=False)
    signal_type = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    metadata = Column(JSON, nullable=True)

class DomainAdapterLog(Base):
    __tablename__ = "domain_adapter_logs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    adapter_name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    response = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class SearchIndexJob(Base):
    __tablename__ = "search_index_jobs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lead_id = Column(UUID(as_uuid=True), nullable=False)
    indexed = Column(Boolean, default=False)

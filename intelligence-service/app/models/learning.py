from sqlalchemy import Column, String, Float, JSON, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.db.base import Base

class LearningMemory(Base):
    __tablename__ = "learning_memory"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    key = Column(String, index=True)
    value = Column(JSON)
    performance_score = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)

class StrategyPerformance(Base):
    __tablename__ = "strategy_performance"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    strategy_name = Column(String, index=True)
    reply_rate = Column(Float, default=0.0)
    conversion_rate = Column(Float, default=0.0)
    metadata_json = Column(JSON)

class StylePattern(Base):
    __tablename__ = "style_patterns"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), nullable=False)
    pattern_type = Column(String) # 'tone', 'hook', 'closing'
    content = Column(String, nullable=False)
    success_count = Column(Float, default=1.0)
    last_used = Column(DateTime, default=datetime.utcnow)

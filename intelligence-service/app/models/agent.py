from sqlalchemy import Column, String, DateTime, func, JSON, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base

class AgentTask(Base):
    __tablename__ = "agent_tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    goal = Column(String, nullable=False)
    status = Column(String, nullable=False, default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class AgentStep(Base):
    __tablename__ = "agent_steps"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task_id = Column(UUID(as_uuid=True), ForeignKey("agent_tasks.id"), nullable=False)
    step_name = Column(String, nullable=False)
    status = Column(String, nullable=False, default="pending")
    result = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class AgentMemory(Base):
    __tablename__ = "agent_memory"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task_id = Column(UUID(as_uuid=True), ForeignKey("agent_tasks.id"), nullable=False)
    key = Column(String, nullable=False)
    value = Column(JSON, nullable=True)

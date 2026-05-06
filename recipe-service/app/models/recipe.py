from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
import uuid
import datetime
from sqlalchemy import DateTime
from app.db.base import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    steps = relationship("RecipeStep", back_populates="recipe", cascade="all, delete")

class RecipeStep(Base):
    __tablename__ = "recipe_steps"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    recipe_id = Column(UUID(as_uuid=True), ForeignKey("recipes.id"), nullable=False)
    step_order = Column(Integer, nullable=False)
    action_type = Column(String, nullable=False) # e.g., 'search_leads', 'extract_contact', 'generate_email'
    config = Column(JSONB, default=dict) # any step-specific configuration
    
    recipe = relationship("Recipe", back_populates="steps")

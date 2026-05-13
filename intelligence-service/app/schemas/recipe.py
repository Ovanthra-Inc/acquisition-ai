from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import List, Optional, Dict, Any
from datetime import datetime

class RecipeStepBase(BaseModel):
    action_type: str
    config: Optional[Dict[str, Any]] = {}

class RecipeStepCreate(RecipeStepBase):
    pass

class RecipeStepResponse(RecipeStepBase):
    id: UUID
    step_order: int
    
    model_config = ConfigDict(from_attributes=True)

class RecipeBase(BaseModel):
    name: str
    description: Optional[str] = None

class RecipeCreate(RecipeBase):
    steps: List[RecipeStepCreate]

class RecipeResponse(RecipeBase):
    id: UUID
    created_at: datetime
    steps: List[RecipeStepResponse]

    model_config = ConfigDict(from_attributes=True)

class RecipeExecuteRequest(BaseModel):
    context: Optional[Dict[str, Any]] = {}

class RecipeExecuteResponse(BaseModel):
    recipe_id: str
    recipe_name: str
    steps_dispatched: List[str]
    status: str
    message: str

from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from uuid import UUID

class RecipeStepCreate(BaseModel):
    step_order: int
    action_type: str
    config: Dict[str, Any] = {}

class RecipeCreate(BaseModel):
    name: str
    description: Optional[str] = None
    steps: List[RecipeStepCreate]

class RecipeStepResponse(BaseModel):
    id: UUID
    step_order: int
    action_type: str
    config: Dict[str, Any]
    
    class Config:
        orm_mode = True

class RecipeResponse(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    steps: List[RecipeStepResponse]
    
    class Config:
        orm_mode = True

class RecipeExecuteRequest(BaseModel):
    context: Optional[Dict[str, Any]] = {}

class RecipeExecuteResponse(BaseModel):
    recipe_id: str
    recipe_name: str
    steps_dispatched: List[str]
    status: str
    message: str


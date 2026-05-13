from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.db.session import get_db
from app.schemas.recipe import RecipeCreate, RecipeResponse, RecipeExecuteRequest, RecipeExecuteResponse
from app.services.recipe_service import RecipeService
from acquisition_core.middleware.auth_middleware import requires_role, requires_tier
from acquisition_core.constants import ROLE_ADMIN, ROLE_MANAGER, TIER_PRO, TIER_ENTERPRISE

router = APIRouter()
service = RecipeService()

@router.post("/", response_model=RecipeResponse, dependencies=[Depends(requires_role([ROLE_ADMIN, ROLE_MANAGER]))])
def create_recipe(request: Request, data: RecipeCreate, db: Session = Depends(get_db)):
    return service.create(db, data)

@router.get("/", response_model=list[RecipeResponse])
def get_recipes(request: Request, db: Session = Depends(get_db)):
    return service.list_recipes(db)

@router.get("/{recipe_id}", response_model=RecipeResponse)
def get_recipe(request: Request, recipe_id: UUID, db: Session = Depends(get_db)):
    recipe = service.get_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.post("/{recipe_id}/execute", response_model=RecipeExecuteResponse, dependencies=[Depends(requires_tier([TIER_PRO, TIER_ENTERPRISE]))])
def execute_recipe(request: Request, recipe_id: UUID, data: RecipeExecuteRequest, db: Session = Depends(get_db)):
    """Execute a recipe by converting its steps into agent steps."""
    user_id = getattr(request.state, "user_id", None)
    recipe = service.get_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return service.execute(db, recipe, data.context or {}, user_id)

@router.post("/{recipe_id}/schedule")
async def schedule_recipe(request: Request, recipe_id: UUID, db: Session = Depends(get_db)):
    """Schedule a recipe to run via Celery eta via the scheduler-service."""
    import httpx
    import datetime
    
    recipe = service.get_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
        
    # In a real app, the run_at time would be passed in the request body.
    # Defaulting to 1 hour from now for this implementation.
    run_at = (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).isoformat()
    
    headers = {"Authorization": f"Bearer {settings.INTERNAL_SERVICE_TOKEN}"}
    payload = {
        "task_name": "app.tasks.agent_tasks.run_recipe_task",
        "run_at": run_at,
        "kwargs": {"recipe_id": str(recipe_id), "context": {}}
    }
    
    async with httpx.AsyncClient() as client:
        res = await client.post("http://scheduler-service:8000/api/v1/scheduler/job", json=payload, headers=headers)
        if res.status_code != 200:
            raise HTTPException(status_code=500, detail=f"Failed to schedule: {res.text}")
            
    return {"message": f"Recipe '{recipe.name}' scheduled for execution", "recipe_id": str(recipe_id), "scheduler_response": res.json()}


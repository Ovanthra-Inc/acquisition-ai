from sqlalchemy.orm import Session
from app.repository.recipe_repo import RecipeRepository
from app.schemas.recipe import RecipeCreate
from uuid import UUID
from typing import Dict, Any, Optional

# Maps recipe action_type → agent executor step name
RECIPE_STEP_MAP = {
    "find_leads":       "search_leads",
    "enrich":           "enrich_lead",
    "score":            "score_lead",
    "generate_email":   "generate_email",
    "create_campaign":  "create_campaign",
    "send_campaign":    "send_email",
    "classify_replies": "classify_reply",
    "get_metrics":      "get_metrics",
    "track_event":      "track_event",
}

class RecipeService:
    def __init__(self):
        self.repo = RecipeRepository()

    def create(self, db: Session, recipe_data: RecipeCreate):
        data = {"name": recipe_data.name, "description": recipe_data.description}
        steps = [step.dict() for step in recipe_data.steps]
        return self.repo.create_recipe(db, data, steps)

    def list_recipes(self, db: Session):
        return self.repo.get_all(db)

    def get_recipe(self, db: Session, recipe_id: UUID):
        return self.repo.get_by_id(db, recipe_id)

    def execute(self, db: Session, recipe, context: Dict[str, Any], user_id: Optional[str]) -> dict:
        """
        Converts recipe steps into a sequence of agent executor step names
        and dispatches them as a Celery task for async execution.
        """
        import os
        from celery import Celery

        # Sort steps by step_order
        sorted_steps = sorted(recipe.steps, key=lambda s: s.step_order)
        step_names = []
        for step in sorted_steps:
            agent_step = RECIPE_STEP_MAP.get(step.action_type, step.action_type)
            step_names.append(agent_step)

        # Enqueue on the default-queue for the agent worker to process
        redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")
        celery_app = Celery("recipe", broker=redis_url)
        celery_app.send_task(
            "app.tasks.agent_tasks.run_recipe_steps",
            args=[str(recipe.id), step_names, context, user_id],
            queue="default-queue"
        )

        return {
            "recipe_id": str(recipe.id),
            "recipe_name": recipe.name,
            "steps_dispatched": step_names,
            "status": "queued",
            "message": f"Recipe '{recipe.name}' dispatched with {len(step_names)} steps."
        }


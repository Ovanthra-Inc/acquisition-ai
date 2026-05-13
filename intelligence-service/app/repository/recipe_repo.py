from app.models.recipe import Recipe, RecipeStep
from acquisition_core.repository import BaseRepository
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Dict, Any

class RecipeRepository(BaseRepository[Recipe]):
    def __init__(self):
        super().__init__(Recipe)

    def create_recipe(self, db: Session, data: Dict[str, Any], steps: List[Dict[str, Any]]) -> Recipe:
        recipe = Recipe(**data)
        db.add(recipe)
        db.flush() # Get the recipe ID
        
        for idx, step_data in enumerate(steps):
            step = RecipeStep(
                recipe_id=recipe.id,
                step_order=idx,
                **step_data
            )
            db.add(step)
        
        db.commit()
        db.refresh(recipe)
        return recipe

    def get_all(self, db: Session) -> List[Recipe]:
        return db.query(Recipe).all()

    def get_by_id(self, db: Session, recipe_id: UUID) -> Recipe:
        return db.query(Recipe).filter(Recipe.id == recipe_id).first()

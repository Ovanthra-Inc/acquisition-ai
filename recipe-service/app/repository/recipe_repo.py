from sqlalchemy.orm import Session
from app.models.recipe import Recipe, RecipeStep
from uuid import UUID

class RecipeRepository:
    def create_recipe(self, db: Session, data: dict, steps_data: list):
        recipe = Recipe(**data)
        db.add(recipe)
        db.flush()
        
        for step in steps_data:
            recipe_step = RecipeStep(recipe_id=recipe.id, **step)
            db.add(recipe_step)
            
        db.commit()
        db.refresh(recipe)
        return recipe

    def get_all(self, db: Session):
        return db.query(Recipe).all()

    def get_by_id(self, db: Session, recipe_id: UUID):
        return db.query(Recipe).filter(Recipe.id == recipe_id).first()

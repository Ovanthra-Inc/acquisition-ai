from fastapi import APIRouter
from app.api.v1.endpoints import agent, recipes, optimization, learning

api_router = APIRouter()
api_router.include_router(agent.router, prefix="/agent", tags=["agent"])
api_router.include_router(recipes.router, prefix="/recipes", tags=["recipes"])
api_router.include_router(optimization.router, prefix="/optimization", tags=["optimization"])
api_router.include_router(learning.router, prefix="/learning", tags=["learning"])

# Stubs for other merged services to maintain API compatibility
@api_router.get("/ai")
def get_ai():
    return {"message": "AI service endpoint (merged)"}

@api_router.get("/recommendations")
def get_recommendations():
    return {"message": "Recommendations endpoint (merged)"}

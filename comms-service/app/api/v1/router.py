from fastapi import APIRouter
from app.api.v1.endpoints import emails, notifications, conversations, social

api_router = APIRouter()
api_router.include_router(emails.router, prefix="/emails", tags=["emails"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
api_router.include_router(conversations.router, prefix="/conversations", tags=["conversations"])
api_router.include_router(social.router, prefix="/social", tags=["social"])

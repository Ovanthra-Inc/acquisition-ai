from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.db.session import get_db
from app.schemas.profile import UserProfileCreateUpdate, UserProfileResponse
from app.services.profile_service import ProfileService

router = APIRouter()
service = ProfileService()

@router.get("/", response_model=UserProfileResponse)
def get_profile(request: Request, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    profile = service.get_profile(db, user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.post("/", response_model=UserProfileResponse)
def create_or_update_profile(request: Request, data: UserProfileCreateUpdate, db: Session = Depends(get_db)):
    user_id = UUID(request.state.user_id)
    return service.upsert_profile(db, user_id, data.dict())

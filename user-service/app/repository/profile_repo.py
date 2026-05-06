from sqlalchemy.orm import Session
from app.models.profile import UserProfile
from uuid import UUID

class ProfileRepository:
    def get_by_user_id(self, db: Session, user_id: UUID):
        return db.query(UserProfile).filter(UserProfile.user_id == user_id).first()

    def upsert(self, db: Session, user_id: UUID, data: dict):
        profile = self.get_by_user_id(db, user_id)
        if profile:
            for key, value in data.items():
                setattr(profile, key, value)
        else:
            profile = UserProfile(user_id=user_id, **data)
            db.add(profile)
        
        db.commit()
        db.refresh(profile)
        return profile

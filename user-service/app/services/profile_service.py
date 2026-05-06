from sqlalchemy.orm import Session
from app.repository.profile_repo import ProfileRepository
from uuid import UUID

class ProfileService:
    def __init__(self):
        self.repo = ProfileRepository()

    def get_profile(self, db: Session, user_id: UUID):
        return self.repo.get_by_user_id(db, user_id)

    def upsert_profile(self, db: Session, user_id: UUID, data: dict):
        return self.repo.upsert(db, user_id, data)

from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    def get_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, email: str):
        user = User(email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

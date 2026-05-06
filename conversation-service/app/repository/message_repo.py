from sqlalchemy.orm import Session
from app.models.message import Message

class MessageRepository:
    def create(self, db: Session, data: dict, classified_as: str):
        msg = Message(**data, classified_as=classified_as)
        db.add(msg)
        db.commit()
        db.refresh(msg)
        return msg

from sqlalchemy.orm import Session
from app.models.conversation import Conversation
from uuid import UUID

class ConversationRepository:
    def create(self, db: Session, user_id: UUID, data: dict):
        conv = Conversation(user_id=user_id, **data)
        db.add(conv)
        db.commit()
        db.refresh(conv)
        return conv

    def get_by_user(self, db: Session, user_id: UUID):
        return db.query(Conversation).filter(Conversation.user_id == user_id).all()

    def get_by_id(self, db: Session, user_id: UUID, conv_id: UUID):
        return db.query(Conversation).filter(Conversation.id == conv_id, Conversation.user_id == user_id).first()

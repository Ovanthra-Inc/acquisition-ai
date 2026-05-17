from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.session import get_db

# Stub repository for message history

class MessageRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_messages(self, conversation_id: UUID, limit: int = 50) -> List[dict]:
        return []

    def create(self, message_data: dict) -> dict:
        return {"id": "test_msg", **message_data}

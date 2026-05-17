from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session

# Stub repository for conversation history

class ConversationRepository:
    def __init__(self, db: Optional[Session] = None):
        self.db = db

    def get_conversation_history(self, lead_id: UUID, limit: int = 50) -> List[dict]:
        return []

    def log_message(self, lead_id: UUID, direction: str, channel: str, content: str) -> dict:
        return {
            "id": "test_msg",
            "lead_id": lead_id,
            "direction": direction,
            "channel": channel,
            "content": content
        }

from sqlalchemy.orm import Session
from app.repository.conversation_repo import ConversationRepository
from app.repository.message_repo import MessageRepository
from app.core.config import settings
from uuid import UUID
import logging

class ConversationService:
    def __init__(self):
        self.conv_repo = ConversationRepository()
        self.msg_repo = MessageRepository()
        
        # Initialize LLM classifier if API key is available
        self._llm = None
        if settings.OPENROUTER_API_KEY:
            from langchain_openai import ChatOpenAI
            self._llm = ChatOpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=settings.OPENROUTER_API_KEY or "dummy_key",
                model="openai/gpt-3.5-turbo",
                temperature=0.0
            )

    def classify(self, message_text: str) -> str:
        # Input sanitization
        if not message_text or len(message_text) > 2000:
            return "neutral"
        
        if self._llm:
            from langchain_core.prompts import PromptTemplate
            prompt = PromptTemplate.from_template(
                """Classify the following email reply into exactly ONE of these categories:
                - interested: The prospect is interested, wants to learn more, or asks about pricing.
                - not_interested: The prospect explicitly declines or says no.
                - more_info_needed: The prospect asks a question or wants more details before deciding.
                - out_of_office: Auto-reply or out-of-office message.
                - opt_out: The prospect asks to unsubscribe or stop being contacted.
                - neutral: Any other reply.
                
                Reply Text: {message_text}
                
                Return ONLY the classification label, nothing else.
                """
            )
            chain = prompt | self._llm
            try:
                response = chain.invoke({"message_text": message_text})
                label = response.content.strip().lower().replace(" ", "_")
                valid = {"interested", "not_interested", "more_info_needed", "out_of_office", "opt_out", "neutral"}
                return label if label in valid else "neutral"
            except Exception as e:
                logging.error(f"LLM classification failed: {e}. Falling back to keyword matching.")
        
        # Keyword fallback
        text = "".join(c for c in message_text.lower() if c.isalnum() or c.isspace())
        if "interested" in text or "yes" in text or "pricing" in text:
            return "interested"
        if "unsubscribe" in text or "stop" in text or "remove" in text:
            return "opt_out"
        return "neutral"

    def handle_reply(self, db: Session, user_id: UUID, data: dict):
        conv = self.conv_repo.get_by_id(db, user_id, data["conversation_id"])
        if not conv:
            raise ValueError("Conversation not found")
            
        classification = self.classify(data["body"])
        return self.msg_repo.create(db, data, classified_as=classification)
        
    def create_conversation(self, db: Session, user_id: UUID, data: dict):
        return self.conv_repo.create(db, user_id, data)

    def get_conversations(self, db: Session, user_id: UUID):
        return self.conv_repo.get_by_user(db, user_id)

    def get_conversation(self, db: Session, user_id: UUID, conv_id: UUID):
        return self.conv_repo.get_by_id(db, user_id, conv_id)


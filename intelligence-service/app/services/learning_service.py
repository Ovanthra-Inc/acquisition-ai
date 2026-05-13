from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from app.core.config import settings
from app.models.learning import StylePattern
from sqlalchemy.orm import Session
from uuid import UUID
import json

class LearningService:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", api_key=settings.OPENAI_API_KEY)
        
    async def extract_winning_patterns(self, db: Session, tenant_id: UUID, original_email: str, positive_reply: str):
        """Analyzes a successful outreach to extract reusable style patterns."""
        prompt = ChatPromptTemplate.from_template("""
        You are an Outreach Optimization Expert. Analyze this successful email interaction.
        
        Original Email Sent: {original}
        Positive Reply Received: {reply}
        
        Identify what worked in the original email. Extract:
        1. The 'Tone' (e.g., authoritative but friendly).
        2. The 'Hook' (the opening line that worked).
        3. The 'Closing' (the call to action that worked).
        
        Respond only in JSON format with keys: 'tone', 'hook', 'closing'.
        """)
        
        chain = prompt | self.llm
        res = await chain.ainvoke({"original": original_email, "reply": positive_reply})
        
        try:
            patterns = json.loads(res.content)
            for p_type, p_content in patterns.items():
                pattern = StylePattern(
                    tenant_id=tenant_id,
                    pattern_type=p_type,
                    content=p_content
                )
                db.add(pattern)
            db.commit()
        except:
            pass # Handle parsing errors gracefully
            
    def get_style_guide(self, db: Session, tenant_id: UUID):
        """Retrieves the aggregated style guide for a tenant."""
        patterns = db.query(StylePattern).filter(StylePattern.tenant_id == tenant_id).all()
        # Aggregation logic here...
        return patterns

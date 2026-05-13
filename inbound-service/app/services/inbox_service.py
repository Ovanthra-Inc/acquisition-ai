from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.core.config import settings
from typing import Dict, Any

class InboxService:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", api_key=settings.OPENAI_API_KEY)
        
    async def classify_reply(self, subject: str, body: str) -> Dict[str, Any]:
        """Classifies an incoming email reply into actionable categories."""
        prompt = ChatPromptTemplate.from_template("""
        You are an AI Acquisition Assistant. Analyze the following email reply and categorize it.
        
        Categories:
        - INTERESTED: The lead wants to talk, book a meeting, or learn more.
        - INFO_REQUEST: The lead has specific questions before proceeding.
        - NOT_INTERESTED: The lead explicitly said no or asked to be removed.
        - OUT_OF_OFFICE: Automated response.
        - OTHER: Anything else.
        
        Email Subject: {subject}
        Email Body: {body}
        
        Provide your response in JSON format with 'category', 'reason', and 'suggested_next_step'.
        """)
        
        chain = prompt | self.llm
        response = await chain.ainvoke({"subject": subject, "body": body})
        
        # In a real app, we would parse the JSON output from the LLM
        # For this implementation, we'll assume a structured output
        return response.content

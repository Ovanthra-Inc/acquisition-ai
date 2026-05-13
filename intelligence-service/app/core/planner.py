from typing import Dict, Any
from app.core.state_manager import AgentState
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.core.config import settings
import json

class PlannerNode:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", api_key=settings.OPENAI_API_KEY)
        
    async def __call__(self, state: AgentState) -> Dict[str, Any]:
        goal = state.get("goal")
        
        prompt = ChatPromptTemplate.from_template("""
        You are an Acquisition Strategist. Create a step-by-step plan to achieve this goal.
        
        Goal: {goal}
        
        Available Tools:
        - search_leads
        - enrich_lead
        - score_lead
        - generate_email
        - create_campaign
        - send_email
        - send_linkedin_message
        - linkedin_connect
        
        Respond only with a JSON array of step names.
        """)
        
        chain = prompt | self.llm
        res = await chain.ainvoke({"goal": goal})
        
        try:
            steps = json.loads(res.content)
            return {"steps": steps, "current_step_index": 0}
        except:
            # Fallback plan
            return {"steps": ["search_leads", "enrich_lead", "generate_email"], "current_step_index": 0}

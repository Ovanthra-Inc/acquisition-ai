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
        goal = state.get("goal", "")
        lead_priority = state.get("context", {}).get("lead_priority", "medium")
        
        prompt = ChatPromptTemplate.from_template("""
        You are an Acquisition Strategist. Create a step-by-step plan to achieve this goal.
        If the lead priority is 'high', prioritize a multi-touch sequence (Email + LinkedIn).
        If the lead priority is 'low', stick to a simple email.
        
        Goal: {goal}
        Lead Priority: {lead_priority}
        
        Available Tools:
        - search_leads
        - enrich_lead (detects tech stack and news)
        - score_lead
        - generate_email
        - linkedin_connect
        - send_linkedin_message
        - send_email
        - send_slack_message
        
        Respond only with a JSON array of tool names.
        """)
        
        chain = prompt | self.llm
        try:
            res = await chain.ainvoke({"goal": goal, "lead_priority": lead_priority})
            # Clean JSON if LLM added markdown
            content = res.content.strip()
            if content.startswith("```json"):
                content = content[7:-3]
            steps = json.loads(content)
            return {"steps": steps, "current_step_index": 0}
        except Exception as e:
            # Fallback plan
            return {"steps": ["search_leads", "enrich_lead", "score_lead", "generate_email", "send_email"], "current_step_index": 0}

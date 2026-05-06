import redis
import json
import os
import logging
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from app.core.config import settings

redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")
redis_client = redis.Redis.from_url(redis_url, decode_responses=True)

class EnrichmentService:
    def __init__(self):
        self.llm = ChatOpenAI(
            openai_api_base="https://openrouter.ai/api/v1",
            openai_api_key=settings.OPENROUTER_API_KEY,
            model_name="openai/gpt-3.5-turbo",
            temperature=0.0
        ) if settings.OPENROUTER_API_KEY else None

    def enrich(self, data: dict):
        website = data.get("website", "")
        if not website:
            return {"industry": "Unknown", "description": "", "pain_points": ""}
            
        cache_key = f"enrichment:{website}"
        cached = redis_client.get(cache_key)
        if cached:
            return json.loads(cached)
        
        if not self.llm:
            logging.warning("OPENROUTER_API_KEY missing. Using fallback enrichment.")
            industry = "SaaS Startup" if ".io" in website else "Software"
            result = {
                "industry": industry,
                "description": f"Automated B2B solutions provider for {industry}",
                "pain_points": "High CAC, low email deliverability, fragmented tools"
            }
            redis_client.setex(cache_key, 3600, json.dumps(result))
            return result

        prompt = PromptTemplate.from_template(
            """Analyze the following company website URL or data to determine their industry, a short description, and likely pain points.
            Company Website/Data: {website}
            
            Return ONLY a valid JSON object with 'industry', 'description', and 'pain_points' keys.
            """
        )
        
        chain = prompt | self.llm
        try:
            response = chain.invoke({"website": website})
            content = response.content.strip()
            if content.startswith("```json"):
                content = content[7:-3]
            elif content.startswith("```"):
                content = content[3:-3]
            result = json.loads(content)
            redis_client.setex(cache_key, 3600, json.dumps(result))
            return result
        except Exception as e:
            logging.error(f"Failed to enrich via LLM: {e}")
            return {"industry": "Unknown", "description": "Failed to analyze", "pain_points": "Unknown"}

    def score(self, data: dict):
        lead_data = data.get("lead_data", {})
        
        if not self.llm:
            score = 50
            if lead_data.get("industry") == "SaaS Startup":
                score += 20
            if lead_data.get("email"):
                score += 30
            return {"score": score}
            
        prompt = PromptTemplate.from_template(
            """You are a Lead Scoring AI. Score the following lead from 0 to 100 based on how likely they are to be a good B2B customer.
            Lead Data: {lead_data}
            
            Return ONLY a valid JSON object with a single 'score' key containing an integer from 0 to 100.
            """
        )
        chain = prompt | self.llm
        try:
            response = chain.invoke({"lead_data": json.dumps(lead_data)})
            content = response.content.strip()
            if content.startswith("```json"):
                content = content[7:-3]
            elif content.startswith("```"):
                content = content[3:-3]
            result = json.loads(content)
            return {"score": int(result.get("score", 50))}
        except Exception as e:
            logging.error(f"Failed to score via LLM: {e}")
            return {"score": 50}

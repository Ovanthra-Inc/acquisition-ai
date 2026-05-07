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
        from langchain_openai import ChatOpenAI
        self.llm = ChatOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.OPENROUTER_API_KEY or "dummy_key",
            model="openai/gpt-3.5-turbo",
            temperature=0.0
        ) if settings.OPENROUTER_API_KEY else None

    def crawl(self, url: str) -> str:
        import httpx
        from bs4 import BeautifulSoup
        try:
            response = httpx.get(url, timeout=10.0, follow_redirects=True)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "lxml")
            
            # Basic cleaning: remove script and style elements
            for script_or_style in soup(["script", "style"]):
                script_or_style.decompose()
                
            text = soup.get_text(separator=" ")
            # Basic cleaning: collapse whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            return " ".join(chunk for chunk in chunks if chunk)
        except Exception as e:
            logging.error(f"Failed to crawl {url}: {e}")
            return f"Error crawling {url}: {str(e)}"

    def enrich(self, data: dict):
        website = data.get("website", "")
        website_text = data.get("website_text", "")
        
        if not website and not website_text:
            return {"industry": "Unknown", "description": "", "pain_points": ""}
            
        cache_key = f"enrichment:{website or hash(website_text)}"
        cached = redis_client.get(cache_key)
        if cached:
            return json.loads(cached)
        
        if not self.llm:
            logging.warning("OPENROUTER_API_KEY missing. Using fallback enrichment.")
            industry = "SaaS Startup" if website and ".io" in website else "Software"
            result = {
                "industry": industry,
                "description": f"Automated B2B solutions provider for {industry}",
                "pain_points": "High CAC, low email deliverability, fragmented tools"
            }
            redis_client.setex(cache_key, 3600, json.dumps(result))
            return result

        from langchain_core.output_parsers import JsonOutputParser
        parser = JsonOutputParser()
        
        prompt = PromptTemplate.from_template(
            """Analyze the following company data to determine their industry, a short description, and likely pain points.
            Company Website: {website}
            Company Website Text (Scraped): {website_text}
            
            Return a valid JSON object with 'industry', 'description', and 'pain_points' keys.
            {format_instructions}
            """
        )
        
        chain = prompt | self.llm | parser
        try:
            result = chain.invoke({
                "website": website, 
                "website_text": website_text[:4000], # Truncate to avoid context window limits
                "format_instructions": parser.get_format_instructions()
            })
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
            
        from langchain_core.output_parsers import JsonOutputParser
        parser = JsonOutputParser()
        
        prompt = PromptTemplate.from_template(
            """You are a Lead Scoring AI. Score the following lead from 0 to 100 based on how likely they are to be a good B2B customer.
            Lead Data: {lead_data}
            
            Return a valid JSON object with a single 'score' key containing an integer from 0 to 100.
            {format_instructions}
            """
        )
        chain = prompt | self.llm | parser
        try:
            result = chain.invoke({
                "lead_data": json.dumps(lead_data),
                "format_instructions": parser.get_format_instructions()
            })
            return {"score": int(result.get("score", 50))}
        except Exception as e:
            logging.error(f"Failed to score via LLM: {e}")
            return {"score": 50}

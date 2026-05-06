from typing import Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from app.core.config import settings
import json
import logging

class AIService:
    def __init__(self):
        # Configure ChatOpenAI to use OpenRouter
        self.llm = ChatOpenAI(
            openai_api_base="https://openrouter.ai/api/v1",
            openai_api_key=settings.OPENROUTER_API_KEY,
            model_name="openai/gpt-3.5-turbo", # Default fallback model on OpenRouter
            temperature=0.7
        )

    def generate_email(self, lead_data: Dict[str, Any], user_profile: Dict[str, Any]) -> dict:
        if not settings.OPENROUTER_API_KEY:
            logging.warning("OPENROUTER_API_KEY is missing. Falling back to dummy generation.")
            return {
                "subject": f"Quick question regarding {lead_data.get('company_name', 'your company')}",
                "body": f"Hi there,\\n\\nI noticed {lead_data.get('company_name', 'your company')} might benefit from {user_profile.get('offer', 'our services')}. Let's chat!\\n\\nBest,\\n"
            }
            
        company = lead_data.get("company_name", "the company")
        industry = lead_data.get("industry", "the industry")
        pain_points = lead_data.get("pain_points", "scaling challenges")
        offer = user_profile.get("offer", "our services")
        
        from langchain_core.output_parsers import JsonOutputParser
        parser = JsonOutputParser()
        
        prompt = PromptTemplate.from_template(
            """You are an expert B2B sales copywriter.
            Write a highly personalized, short, and engaging cold email.
            
            Context:
            Lead Company: {company}
            Lead Industry: {industry}
            Lead Pain Points: {pain_points}
            Our Offer: {offer}
            
            Return a valid JSON object with 'subject' and 'body' keys.
            {format_instructions}
            """
        )
        
        chain = prompt | self.llm | parser
        
        try:
            return chain.invoke({
                "company": company,
                "industry": industry,
                "pain_points": pain_points,
                "offer": offer,
                "format_instructions": parser.get_format_instructions()
            })
        except Exception as e:
            logging.error(f"Failed to parse LLM response: {e}.")
            return {
                "subject": f"Quick question regarding {company}",
                "body": f"Hi there,\\n\\nI noticed {company} might benefit from {offer}. Let's chat!\\n\\nBest,\\n"
            }

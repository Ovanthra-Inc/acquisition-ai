from typing import Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from app.core.config import settings
import json
import logging

from app.services.persona_service import PersonaService

class AIService:
    def __init__(self):
        self.llm = ChatOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.OPENROUTER_API_KEY or "dummy_key",
            model="openai/gpt-3.5-turbo",
            temperature=0.7
        )
        self.persona_service = PersonaService()

    def generate_email(self, lead_data: Dict[str, Any], user_profile: Dict[str, Any], persona: str = "consultative") -> dict:
        if not settings.OPENROUTER_API_KEY:
            return {
                "subject": f"Quick question regarding {lead_data.get('company_name', 'your company')}",
                "body": f"Hi there,\\n\\nI noticed {lead_data.get('company_name', 'your company')} might benefit from {user_profile.get('offer', 'our services')}. Let's chat!\\n\\nBest,\\n"
            }
            
        company = lead_data.get("company_name", "the company")
        industry = lead_data.get("industry", "the industry")
        pain_points = lead_data.get("pain_points", "scaling challenges")
        offer = user_profile.get("offer", "our services")
        persona_context = self.persona_service.get_prompt_context(persona)
        
        from langchain_core.output_parsers import JsonOutputParser
        parser = JsonOutputParser()
        
        prompt = PromptTemplate.from_template(
            """You are an expert B2B sales copywriter.
            {persona_context}
            
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
                "persona_context": persona_context,
                "format_instructions": parser.get_format_instructions()
            })
        except Exception as e:
            logging.error(f"Failed to generate email: {e}")
            return {"subject": f"Quick question regarding {company}", "body": "Hi there..."}

    def generate_outreach_sequence(self, lead_data: Dict[str, Any], user_profile: Dict[str, Any], persona: str = "consultative") -> dict:
        """Generates a 2-step sequence: Email 1 followed by a LinkedIn connection note."""
        email = self.generate_email(lead_data, user_profile, persona)
        
        # Simple LinkedIn note generation
        persona_context = self.persona_service.get_prompt_context(persona)
        prompt = PromptTemplate.from_template(
            """{persona_context}
            Write a short (under 300 characters) LinkedIn connection note for {company_name}.
            Reference their use of {tech_stack} or recent news: {recent_news}.
            """
        )
        chain = prompt | self.llm
        try:
            li_res = chain.invoke({
                "company_name": lead_data.get("company_name", "the company"),
                "tech_stack": lead_data.get("tech_stack", ["modern tech"]),
                "recent_news": lead_data.get("recent_news", "growth"),
                "persona_context": persona_context
            })
            li_note = li_res.content
        except:
            li_note = "Hi! Noticed your work in the industry and wanted to connect."

        return {
            "email": email,
            "linkedin_note": li_note,
            "persona": persona
        }

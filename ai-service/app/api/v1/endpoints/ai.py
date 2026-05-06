from fastapi import APIRouter, Depends, Request
from app.schemas.ai import GenerateEmailRequest, GenerateEmailResponse
from app.services.ai_service import AIService

router = APIRouter()
service = AIService()

@router.post("/generate-email", response_model=GenerateEmailResponse)
def generate_email(request: Request, data: GenerateEmailRequest):
    # Here we might log usage against the user_id for billing purposes
    user_id = request.state.user_id
    result = service.generate_email(data.lead_data, data.user_profile)
    return result

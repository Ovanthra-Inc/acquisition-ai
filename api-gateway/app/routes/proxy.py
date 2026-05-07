from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from starlette.background import BackgroundTask
import httpx
from app.utils.signature import generate_signature
from app.core.config import settings

router = APIRouter()

SERVICE_MAP = {
    "/api/v1/auth": settings.AUTH_SERVICE_URL,
    "/api/v1/users": settings.USER_SERVICE_URL,
    "/api/v1/leads": settings.LEAD_SERVICE_URL,
    "/api/v1/campaigns": settings.CAMPAIGN_SERVICE_URL,
    "/api/v1/emails": settings.EMAIL_SERVICE_URL,
    "/api/v1/ai": settings.AI_SERVICE_URL,
    "/api/v1/agent": settings.AGENT_SERVICE_URL,
    "/api/v1/recipes": settings.RECIPE_SERVICE_URL,
    "/api/v1/enrichment": settings.ENRICHMENT_SERVICE_URL,
    "/api/v1/conversations": settings.CONVERSATION_SERVICE_URL,
    "/api/v1/analytics": settings.ANALYTICS_SERVICE_URL,
    "/api/v1/notifications": settings.NOTIFICATION_SERVICE_URL,
    "/api/v1/scheduler": settings.SCHEDULER_SERVICE_URL,
    "/api/v1/domains": settings.DOMAIN_SERVICE_URL,
    "/api/v1/sources": settings.DOMAIN_SERVICE_URL,
    "/api/v1/signals": settings.DOMAIN_SERVICE_URL,
    "/api/v1/deliverability": settings.DELIVERABILITY_SERVICE_URL,
    "/api/v1/limits": settings.RATE_LIMITING_SERVICE_URL,
    "/api/v1/security": settings.SECURITY_SERVICE_URL,
    "/api/v1/proxy": settings.PROXY_SERVICE_URL,
    "/api/v1/system": settings.OBSERVABILITY_SERVICE_URL,
    "/api/v1/optimization": settings.OPTIMIZATION_SERVICE_URL,
    "/api/v1/experiment": settings.EXPERIMENTATION_SERVICE_URL,
    "/api/v1/learning": settings.LEARNING_SERVICE_URL,
    "/api/v1/pipeline": settings.PIPELINE_SERVICE_URL,
    "/api/v1/recommendations": settings.RECOMMENDATION_SERVICE_URL,
    "/api/v1/organizations": settings.ORGANIZATION_SERVICE_URL,
    "/api/v1/roles": settings.RBAC_SERVICE_URL,
    "/api/v1/audit": settings.AUDIT_SERVICE_URL,
    "/api/v1/api-keys": settings.PLATFORM_API_SERVICE_URL,
    "/api/v1/webhooks": settings.PLATFORM_API_SERVICE_URL,
    "/api/v1/policies": settings.POLICY_SERVICE_URL,
    "/api/v1/billing": settings.BILLING_SERVICE_URL,
    "/api/v1/dashboard": settings.BFF_SERVICE_URL,
}

@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy(request: Request, path: str):

    url_path = f"/{path}"

    for route, service_url in SERVICE_MAP.items():
        if url_path.startswith(route):
            # Pass the rest of the path to the downstream service
            target_url = service_url + url_path
            break
    else:
        return {"error": "Route not found"}

    user = getattr(request.state, "user", {})
    user_id = str(user.get("user_id", ""))
    tenant_id = str(user.get("tenant_id", ""))

    headers = dict(request.headers)
    # Remove host header to avoid confusion downstream
    headers.pop("host", None)
    
    # SECURITY: Strip ALL internal headers from client request to prevent injection.
    # An attacker could send X-User-Id: admin to impersonate users.
    STRIP_HEADERS = [
        "x-user-id", "x-tenant-id", "x-service-name", 
        "x-request-signature", "x-roles", "x-forwarded-for"
    ]
    headers = {k: v for k, v in headers.items() if k.lower() not in STRIP_HEADERS}

    # Inject trusted internal headers (these override anything the client sent)
    headers.update({
        "X-User-Id": user_id,
        "X-Tenant-Id": tenant_id,
        "X-Service-Name": "api-gateway",
        "Authorization": f"Bearer {settings.INTERNAL_SERVICE_TOKEN}",
        "X-Request-Signature": generate_signature(user_id, tenant_id, "api-gateway"),
        "X-Forwarded-For": request.client.host if request.client else "",
    })

    client = httpx.AsyncClient(timeout=60.0)
    
    # Avoid passing the client request body if GET
    content = request.stream() if request.method not in ["GET", "HEAD"] else None
    
    req = client.build_request(
        request.method,
        target_url,
        headers=headers,
        content=content,
        params=request.query_params
    )
    
    response = await client.send(req, stream=True)
    
    # Exclude headers that might cause issues when proxying
    excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
    response_headers = {k: v for k, v in response.headers.items() if k.lower() not in excluded_headers}

    async def aclose_client():
        await response.aclose()
        await client.aclose()

    return StreamingResponse(
        response.aiter_raw(),
        status_code=response.status_code,
        headers=response_headers,
        background=BackgroundTask(aclose_client)
    )

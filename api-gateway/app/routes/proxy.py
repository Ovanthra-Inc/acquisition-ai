from fastapi import APIRouter, Request
import httpx
from app.utils.signature import generate_signature
from app.core.config import settings

router = APIRouter()

SERVICE_MAP = {
    "/api/v1/auth": "http://auth-service:8000",
    "/api/v1/users": "http://user-service:8000",
    "/api/v1/leads": "http://lead-service:8000",
    "/api/v1/campaigns": "http://campaign-service:8000",
    "/api/v1/emails": "http://email-service:8000",
    "/api/v1/ai": "http://ai-service:8000",
    "/api/v1/agent": "http://agent-service:8000",
    "/api/v1/recipes": "http://recipe-service:8000",
    "/api/v1/enrichment": "http://enrichment-service:8000",
    "/api/v1/conversations": "http://conversation-service:8000",
    "/api/v1/analytics": "http://analytics-service:8000",
    "/api/v1/notifications": "http://notification-service:8000",
    "/api/v1/scheduler": "http://scheduler-service:8000",
    "/api/v1/domains": "http://domain-service:8000",
    "/api/v1/sources": "http://domain-service:8000",
    "/api/v1/signals": "http://domain-service:8000",
    "/api/v1/deliverability": "http://deliverability-service:8000",
    "/api/v1/limits": "http://rate-limiting-service:8000",
    "/api/v1/security": "http://security-service:8000",
    "/api/v1/proxy": "http://proxy-service:8000",
    "/api/v1/system": "http://observability-service:8000",
    "/api/v1/optimization": "http://optimization-service:8000",
    "/api/v1/experiment": "http://experimentation-service:8000",
    "/api/v1/learning": "http://learning-service:8000",
    "/api/v1/pipeline": "http://pipeline-service:8000",
    "/api/v1/recommendations": "http://recommendation-service:8000",
    "/api/v1/organizations": "http://organization-service:8000",
    "/api/v1/roles": "http://rbac-service:8000",
    "/api/v1/audit": "http://audit-service:8000",
    "/api/v1/api-keys": "http://platform-api-service:8000",
    "/api/v1/webhooks": "http://platform-api-service:8000",
    "/api/v1/policies": "http://policy-service:8000",
    "/api/v1/billing": "http://billing-service:8000",
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

    async with httpx.AsyncClient(timeout=10.0) as client:
        # Avoid passing the client request body if GET
        body = await request.body()
        if request.method in ["GET", "HEAD"]:
            body = None
            
        response = await client.request(
            request.method,
            target_url,
            headers=headers,
            content=body,
            params=request.query_params
        )

    # Return the exact status code and content from downstream
    from fastapi.responses import Response
    return Response(content=response.content, status_code=response.status_code, headers=dict(response.headers))

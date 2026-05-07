import asyncio
from acquisition_core.client import get_internal_client
from app.core.config import settings

class DashboardService:
    async def get_dashboard_data(self, user_id: str, tenant_id: str, signature: str):
        async with get_internal_client(settings.INTERNAL_SERVICE_TOKEN, user_id, tenant_id, "bff-service") as client:
            # Aggregate multiple service calls concurrently
            tasks = [
                client.get(f"{settings.USER_SERVICE_URL}/api/v1/users/me"),
                client.get(f"{settings.CAMPAIGN_SERVICE_URL}/api/v1/campaigns/"),
                client.get(f"{settings.ANALYTICS_SERVICE_URL}/api/v1/analytics/overview"),
                client.get(f"{settings.NOTIFICATION_SERVICE_URL}/api/v1/notifications/"),
                client.get(f"{settings.AGENT_SERVICE_URL}/api/v1/agent/tasks") 
            ]
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            def get_json(res):
                if isinstance(res, Exception) or res.status_code != 200:
                    return {}
                return res.json()

            return {
                "user": get_json(results[0]),
                "campaigns": get_json(results[1]),
                "analytics": get_json(results[2]),
                "notifications": get_json(results[3]),
                "agent_tasks": get_json(results[4])
            }

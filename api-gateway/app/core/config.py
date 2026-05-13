from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Api Gateway"
    API_V1_STR: str = "/api/v1"
    
    # Gateway settings
    JWT_SECRET: str = "supersecret"
    INTERNAL_SERVICE_TOKEN: str = "internal-secret"
    REDIS_URL: str = "redis://localhost:6379"
    
    # Service URLs
    AUTH_SERVICE_URL: str = "http://identity-service:8000"
    USER_SERVICE_URL: str = "http://identity-service:8000"
    LEAD_SERVICE_URL: str = "http://marketing-service:8000"
    CAMPAIGN_SERVICE_URL: str = "http://marketing-service:8000"
    EMAIL_SERVICE_URL: str = "http://comms-service:8000"
    AI_SERVICE_URL: str = "http://intelligence-service:8000"
    AGENT_SERVICE_URL: str = "http://intelligence-service:8000"
    RECIPE_SERVICE_URL: str = "http://intelligence-service:8000"
    ENRICHMENT_SERVICE_URL: str = "http://marketing-service:8000"
    CONVERSATION_SERVICE_URL: str = "http://comms-service:8000"
    ANALYTICS_SERVICE_URL: str = "http://ops-service:8000"
    NOTIFICATION_SERVICE_URL: str = "http://comms-service:8000"
    SCHEDULER_SERVICE_URL: str = "http://scheduler-service:8000"
    DOMAIN_SERVICE_URL: str = "http://marketing-service:8000"
    DELIVERABILITY_SERVICE_URL: str = "http://marketing-service:8000"
    RATE_LIMITING_SERVICE_URL: str = "http://ops-service:8000"
    SECURITY_SERVICE_URL: str = "http://identity-service:8000"
    PROXY_SERVICE_URL: str = "http://ops-service:8000"
    OBSERVABILITY_SERVICE_URL: str = "http://ops-service:8000"
    OPTIMIZATION_SERVICE_URL: str = "http://intelligence-service:8000"
    EXPERIMENTATION_SERVICE_URL: str = "http://ops-service:8000"
    LEARNING_SERVICE_URL: str = "http://intelligence-service:8000"
    PIPELINE_SERVICE_URL: str = "http://marketing-service:8000"
    RECOMMENDATION_SERVICE_URL: str = "http://intelligence-service:8000"
    ORGANIZATION_SERVICE_URL: str = "http://identity-service:8000"
    RBAC_SERVICE_URL: str = "http://identity-service:8000"
    AUDIT_SERVICE_URL: str = "http://ops-service:8000"
    PLATFORM_API_SERVICE_URL: str = "http://ops-service:8000"
    POLICY_SERVICE_URL: str = "http://identity-service:8000"
    BILLING_SERVICE_URL: str = "http://identity-service:8000"
    BFF_SERVICE_URL: str = "http://api-gateway:8000"

    class Config:
        env_file = ".env"
        extra = "ignore"
        case_sensitive = True

settings = Settings()




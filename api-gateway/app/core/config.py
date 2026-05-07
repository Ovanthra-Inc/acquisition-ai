from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Api Gateway"
    API_V1_STR: str = "/api/v1"
    
    # Gateway settings
    JWT_SECRET: str = "supersecret"
    INTERNAL_SERVICE_TOKEN: str = "internal-secret"
    REDIS_URL: str = "redis://localhost:6379"
    
    # Database settings (if gateway needs DB, currently it shouldn't)
    POSTGRES_SERVER: str = "db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "acquisition"
    
    @property
    def DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"
    
    # Service URLs
    AUTH_SERVICE_URL: str = "http://auth-service:8000"
    USER_SERVICE_URL: str = "http://user-service:8000"
    LEAD_SERVICE_URL: str = "http://lead-service:8000"
    CAMPAIGN_SERVICE_URL: str = "http://campaign-service:8000"
    EMAIL_SERVICE_URL: str = "http://email-service:8000"
    AI_SERVICE_URL: str = "http://ai-service:8000"
    AGENT_SERVICE_URL: str = "http://agent-service:8000"
    RECIPE_SERVICE_URL: str = "http://recipe-service:8000"
    ENRICHMENT_SERVICE_URL: str = "http://enrichment-service:8000"
    CONVERSATION_SERVICE_URL: str = "http://conversation-service:8000"
    ANALYTICS_SERVICE_URL: str = "http://analytics-service:8000"
    NOTIFICATION_SERVICE_URL: str = "http://notification-service:8000"
    SCHEDULER_SERVICE_URL: str = "http://scheduler-service:8000"
    DOMAIN_SERVICE_URL: str = "http://domain-service:8000"
    DELIVERABILITY_SERVICE_URL: str = "http://deliverability-service:8000"
    RATE_LIMITING_SERVICE_URL: str = "http://rate-limiting-service:8000"
    SECURITY_SERVICE_URL: str = "http://security-service:8000"
    PROXY_SERVICE_URL: str = "http://proxy-service:8000"
    OBSERVABILITY_SERVICE_URL: str = "http://observability-service:8000"
    OPTIMIZATION_SERVICE_URL: str = "http://optimization-service:8000"
    EXPERIMENTATION_SERVICE_URL: str = "http://experimentation-service:8000"
    LEARNING_SERVICE_URL: str = "http://learning-service:8000"
    PIPELINE_SERVICE_URL: str = "http://pipeline-service:8000"
    RECOMMENDATION_SERVICE_URL: str = "http://recommendation-service:8000"
    ORGANIZATION_SERVICE_URL: str = "http://organization-service:8000"
    RBAC_SERVICE_URL: str = "http://rbac-service:8000"
    AUDIT_SERVICE_URL: str = "http://audit-service:8000"
    PLATFORM_API_SERVICE_URL: str = "http://platform-api-service:8000"
    POLICY_SERVICE_URL: str = "http://policy-service:8000"
    BILLING_SERVICE_URL: str = "http://billing-service:8000"
    BFF_SERVICE_URL: str = "http://bff-service:8000"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

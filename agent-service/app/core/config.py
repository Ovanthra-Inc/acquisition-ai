from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Agent Service"
    API_V1_STR: str = "/api/v1"
    
    # Database settings
    POSTGRES_SERVER: str = "db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "acquisition"
    
    REDIS_URL: str = "redis://redis:6379/0"
    INTERNAL_SERVICE_TOKEN: str = "supersecrettoken"
    
    @property
    def DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"
    
    # Internal Service URLs
    DOMAIN_SERVICE_URL: str = "http://domain-service:8000"
    LEAD_SERVICE_URL: str = "http://lead-service:8000"
    ENRICHMENT_SERVICE_URL: str = "http://enrichment-service:8000"
    CAMPAIGN_SERVICE_URL: str = "http://campaign-service:8000"
    AI_SERVICE_URL: str = "http://ai-service:8000"
    CONVERSATION_SERVICE_URL: str = "http://conversation-service:8000"
    ANALYTICS_SERVICE_URL: str = "http://analytics-service:8000"
    SCHEDULER_SERVICE_URL: str = "http://scheduler-service:8000"
    DELIVERABILITY_SERVICE_URL: str = "http://deliverability-service:8000"
    RECIPE_SERVICE_URL: str = "http://recipe-service:8000"
    AUDIT_SERVICE_URL: str = "http://audit-service:8000"
    EXPERIMENT_SERVICE_URL: str = "http://experimentation-service:8000"
    LEARNING_SERVICE_URL: str = "http://learning-service:8000"
    ORGANIZATION_SERVICE_URL: str = "http://organization-service:8000"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Agent Service"
    API_V1_STR: str = "/api/v1"
    
    # Database settings
    POSTGRES_SERVER: str = "db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "acquisition"
    ALEMBIC_VERSION_TABLE: str = "alembic_version_intelligence_service"
    
    REDIS_URL: str = "redis://redis:6379/0"
    INTERNAL_SERVICE_TOKEN: str = "supersecrettoken"
    OPENAI_API_KEY: str = ""
    
    @property
    def DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"
    
    # Internal Service URLs
    DOMAIN_SERVICE_URL: str = "http://marketing-service:8000"
    LEAD_SERVICE_URL: str = "http://marketing-service:8000"
    ENRICHMENT_SERVICE_URL: str = "http://marketing-service:8000"
    CAMPAIGN_SERVICE_URL: str = "http://marketing-service:8000"
    AI_SERVICE_URL: str = "http://intelligence-service:8000"
    EMAIL_SERVICE_URL: str = "http://comms-service:8000"
    CONVERSATION_SERVICE_URL: str = "http://comms-service:8000"
    ANALYTICS_SERVICE_URL: str = "http://ops-service:8000"
    SCHEDULER_SERVICE_URL: str = "http://scheduler-service:8000"
    DELIVERABILITY_SERVICE_URL: str = "http://marketing-service:8000"
    RECIPE_SERVICE_URL: str = "http://intelligence-service:8000"
    AUDIT_SERVICE_URL: str = "http://ops-service:8000"
    EXPERIMENT_SERVICE_URL: str = "http://experimentation-service:8000"
    LEARNING_SERVICE_URL: str = "http://intelligence-service:8000"
    ORGANIZATION_SERVICE_URL: str = "http://identity-service:8000"

    class Config:
        env_file = ".env"
        extra = "ignore"
        case_sensitive = True

settings = Settings()





from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Worker"
    API_V1_STR: str = "/api/v1"
    
    # Database settings
    POSTGRES_SERVER: str = "db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "acquisition"
    ALEMBIC_VERSION_TABLE: str = "alembic_version_worker"
    
    @property
    def DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"
    
    INTERNAL_SERVICE_TOKEN: str = "supersecrettoken"
    EMAIL_SERVICE_URL: str = "http://comms-service:8000"
    ENRICHMENT_SERVICE_URL: str = "http://marketing-service:8000"
    CONVERSATION_SERVICE_URL: str = "http://comms-service:8000"
    AGENT_SERVICE_URL: str = "http://intelligence-service:8000"

    class Config:
        env_file = ".env"
        extra = "ignore"
        case_sensitive = True

settings = Settings()




from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Worker"
    API_V1_STR: str = "/api/v1"
    
    # Database settings
    POSTGRES_SERVER: str = "db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "acquisition"
    
    @property
    def DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"
    
    INTERNAL_SERVICE_TOKEN: str = "supersecrettoken"
    EMAIL_SERVICE_URL: str = "http://email-service:8000"
    ENRICHMENT_SERVICE_URL: str = "http://enrichment-service:8000"
    CONVERSATION_SERVICE_URL: str = "http://conversation-service:8000"
    AGENT_SERVICE_URL: str = "http://agent-service:8000"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

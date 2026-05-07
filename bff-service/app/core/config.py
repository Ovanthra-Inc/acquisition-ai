from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "BFF Service"
    INTERNAL_SERVICE_TOKEN: str = "supersecrettoken"

    USER_SERVICE_URL: str = "http://user-service:8000"
    CAMPAIGN_SERVICE_URL: str = "http://campaign-service:8000"
    ANALYTICS_SERVICE_URL: str = "http://analytics-service:8000"
    NOTIFICATION_SERVICE_URL: str = "http://notification-service:8000"
    AGENT_SERVICE_URL: str = "http://agent-service:8000"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

from pydantic_settings import BaseSettings
from typing import Optional

class GlobalSettings(BaseSettings):
    PROJECT_NAME: str = "Acquisition AI"
    API_V1_STR: str = "/api/v1"
    
    # Core Infrastructure
    INTERNAL_SERVICE_TOKEN: str = "internal-secret"
    JWT_SECRET: str = "your-secret-key"
    
    # PostgreSQL
    POSTGRES_SERVER: str = "db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "acquisition"
    
    # Redis
    REDIS_URL: str = "redis://redis:6379/0"
    
    @property
    def DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"

    class Config:
        env_file = ".env"
        extra = "ignore"
        case_sensitive = True

settings = GlobalSettings()

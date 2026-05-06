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
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

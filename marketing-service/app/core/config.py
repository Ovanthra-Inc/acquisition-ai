from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Lead Service"
    API_V1_STR: str = "/api/v1"
    INTERNAL_SERVICE_TOKEN: str = "your_default_token"
    
    # Database settings
    POSTGRES_SERVER: str = "db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "acquisition"
    ALEMBIC_VERSION_TABLE: str = "alembic_version_marketing_service"
    
    @property
    def DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"
    
    class Config:
        env_file = ".env"
        extra = "ignore"
        case_sensitive = True

settings = Settings()



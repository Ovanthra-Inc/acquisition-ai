from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Auth Service"
    API_V1_STR: str = "/api/v1"
    
    # Internal & JWT Settings
    JWT_SECRET: str = "supersecret"
    INTERNAL_SERVICE_TOKEN: str = "internal-secret"
    
    # Google OAuth
    GOOGLE_CLIENT_ID: str = "dummy_google_client_id"
    GOOGLE_CLIENT_SECRET: str = "dummy_google_client_secret"
    GOOGLE_CALLBACK_URL: str = "http://localhost:8000/api/v1/auth/callback/google" # API gateway URL
    
    # Database settings
    POSTGRES_SERVER: str = "db" # or "postgres" in docker
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "acquisition"
    ALEMBIC_VERSION_TABLE: str = "alembic_version_identity_service"
    
    @property
    def DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"
    
    class Config:
        env_file = ".env"
        extra = "ignore"
        case_sensitive = True

settings = Settings()



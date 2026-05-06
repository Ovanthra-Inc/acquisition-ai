import os

services = [
    "api-gateway",
    "auth-service",
    "user-service",
    "lead-service",
    "campaign-service",
    "email-service",
    "ai-service",
    "agent-service",
    "recipe-service",
    "worker"
]

folders = [
    "app",
    "app/api/v1/endpoints",
    "app/core",
    "app/models",
    "app/schemas",
    "app/repository",
    "app/services",
    "app/db",
    "app/utils"
]

def create_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

base_dir = r"c:\Users\ashut\Devlopments\acquisition\acquisition"

for service in services:
    service_dir = os.path.join(base_dir, service)
    os.makedirs(service_dir, exist_ok=True)
    
    # Create folders
    for folder in folders:
        folder_path = os.path.join(service_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        # Create __init__.py files to make them python modules
        create_file(os.path.join(folder_path, "__init__.py"), "")

    # Create main.py
    main_content = f"""from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title="{service.replace('-', ' ').title()}")

@app.get("/")
def read_root():
    return {{"message": f"Welcome to {{settings.PROJECT_NAME}}"}}
"""
    if service != "worker":
        create_file(os.path.join(service_dir, "app", "main.py"), main_content)

    # Create core/config.py
    config_content = f"""from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "{service.replace('-', ' ').title()}"
    API_V1_STR: str = "/api/v1"
    
    # Database settings
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "acquisition"
    
    @property
    def DATABASE_URI(self) -> str:
        return f"postgresql://{{self.POSTGRES_USER}}:{{self.POSTGRES_PASSWORD}}@{{self.POSTGRES_SERVER}}/{{self.POSTGRES_DB}}"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
"""
    create_file(os.path.join(service_dir, "app", "core", "config.py"), config_content)
    
    # Create db/base.py
    base_db_content = """from sqlalchemy.orm import declarative_base

Base = declarative_base()
"""
    create_file(os.path.join(service_dir, "app", "db", "base.py"), base_db_content)

    # Create db/session.py
    session_db_content = """from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""
    create_file(os.path.join(service_dir, "app", "db", "session.py"), session_db_content)

    # Create endpoints.md
    endpoints_content = f"""# {service.replace('-', ' ').title()} Endpoints

List of API endpoints exposed by this service.

## Base URL
`/api/v1`

## Endpoints
* `GET /` - Health check
"""
    create_file(os.path.join(service_dir, "endpoints.md"), endpoints_content)

    # Create features.md
    features_content = f"""# {service.replace('-', ' ').title()} Features

List of features handled by this service according to Phase 1 requirements.

## Core Responsibilities
* Replace with actual features for {service}
"""
    create_file(os.path.join(service_dir, "features.md"), features_content)

    # Create requirements.txt
    req_content = """fastapi
uvicorn
pydantic
pydantic-settings
sqlalchemy
psycopg2-binary
alembic
"""
    create_file(os.path.join(service_dir, "requirements.txt"), req_content)

print("Scaffolding complete.")

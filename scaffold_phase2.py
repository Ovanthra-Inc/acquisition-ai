import os

services = [
    "enrichment-service",
    "conversation-service",
    "analytics-service",
    "notification-service"
]

folders = [
    "app/api/v1/endpoints",
    "app/core",
    "app/models",
    "app/schemas",
    "app/services",
    "app/repository",
    "app/db"
]

base_dir = r"c:\Users\ashut\Devlopments\acquisition\acquisition"

for service in services:
    service_path = os.path.join(base_dir, service)
    os.makedirs(service_path, exist_ok=True)
    
    for folder in folders:
        os.makedirs(os.path.join(service_path, folder), exist_ok=True)
        init_file = os.path.join(service_path, folder, "__init__.py")
        if not os.path.exists(init_file):
            open(init_file, "a").close()
            
    # Base configuration
    db_base = """from sqlalchemy.ext.declarative import declarative_base\n\nBase = declarative_base()"""
    with open(os.path.join(service_path, "app", "db", "base.py"), "w") as f:
        f.write(db_base)
        
    db_session = """from sqlalchemy import create_engine\nfrom sqlalchemy.orm import sessionmaker\nfrom app.core.config import settings\n\nengine = create_engine(settings.DATABASE_URI)\nSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)\n\ndef get_db():\n    db = SessionLocal()\n    try:\n        yield db\n    finally:\n        db.close()\n"""
    with open(os.path.join(service_path, "app", "db", "session.py"), "w") as f:
        f.write(db_session)
        
    config = """from pydantic_settings import BaseSettings\n\nclass Settings(BaseSettings):\n    PROJECT_NAME: str = \"""" + service.replace("-", " ").title() + """\"\n    API_V1_STR: str = \"/api/v1\"\n    INTERNAL_SERVICE_TOKEN: str = \"internal-secret\"\n    POSTGRES_SERVER: str = \"localhost\"\n    POSTGRES_USER: str = \"postgres\"\n    POSTGRES_PASSWORD: str = \"postgres\"\n    POSTGRES_DB: str = \"acquisition\"\n    \n    @property\n    def DATABASE_URI(self) -> str:\n        return f\"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}\"\n    \n    class Config:\n        env_file = \".env\"\n        case_sensitive = True\n\nsettings = Settings()"""
    with open(os.path.join(service_path, "app", "core", "config.py"), "w") as f:
        f.write(config)

    reqs = """fastapi\nuvicorn\npydantic\npydantic-settings\nsqlalchemy\npsycopg2-binary\nalembic\nhttpx\n"""
    with open(os.path.join(service_path, "requirements.txt"), "w") as f:
        f.write(reqs)

print("Phase 2 scaffolding complete.")

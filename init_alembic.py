import os
import subprocess
import sys

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
    "worker",
    "enrichment-service",
    "conversation-service",
    "analytics-service",
    "notification-service"
]

base_dir = r"c:\Users\ashut\Devlopments\acquisition\acquisition"

for service in services:
    service_dir = os.path.join(base_dir, service)
    os.chdir(service_dir)
    subprocess.run([sys.executable, "-m", "alembic", "init", "alembic"])
    
    # modify alembic.ini to set version_table
    alembic_ini_path = "alembic.ini"
    with open(alembic_ini_path, "r") as f:
        content = f.read()
    
    table_name = service.replace("-", "_") + "_alembic_version"
    content = content.replace("# version_table = alembic_version", f"version_table = {table_name}")
    content = content.replace("sqlalchemy.url = driver://user:pass@localhost/dbname", 'sqlalchemy.url = postgresql://postgres:postgres@localhost/acquisition')
    
    with open(alembic_ini_path, "w") as f:
        f.write(content)
        
    # modify env.py to import the models and set target_metadata
    env_py_path = "alembic/env.py"
    with open(env_py_path, "r") as f:
        env_content = f.read()
        
    env_content = env_content.replace(
        "target_metadata = None",
        "import sys\nimport os\nsys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))\nfrom app.db.base import Base\n\n# Import all models here so they are registered with Base.metadata\n# from app.models.example import ExampleModel\n\ntarget_metadata = Base.metadata"
    )
    
    with open(env_py_path, "w") as f:
        f.write(env_content)

os.chdir(base_dir)

# Create the master auto-migrate script
migrate_script = """import os
import subprocess
import sys

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
    "worker",
    "enrichment-service",
    "conversation-service",
    "analytics-service",
    "notification-service"
]

base_dir = os.path.dirname(os.path.abspath(__file__))

for service in services:
    print(f"\\n--- Running migrations for {service} ---")
    service_dir = os.path.join(base_dir, service)
    os.chdir(service_dir)
    
    # Try to autogenerate.
    res = subprocess.run([sys.executable, "-m", "alembic", "revision", "--autogenerate", "-m", "auto_migration"], capture_output=True, text=True)
    if "Target database is not up to date" in res.stderr:
        print(f"Warning: Database not up to date for {service}. Upgrading first...")
        subprocess.run([sys.executable, "-m", "alembic", "upgrade", "head"])
        subprocess.run([sys.executable, "-m", "alembic", "revision", "--autogenerate", "-m", "auto_migration"])
        
    print(res.stdout)
    if res.stderr:
        print(res.stderr, file=sys.stderr)
        
    # Upgrade to head
    subprocess.run([sys.executable, "-m", "alembic", "upgrade", "head"])

print("\\n✅ All migrations complete.")
"""

with open("auto_migrate.py", "w", encoding="utf-8") as f:
    f.write(migrate_script)

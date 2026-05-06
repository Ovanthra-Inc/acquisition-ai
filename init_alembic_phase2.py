import os
import subprocess
import sys

new_services = [
    "conversation-service",
    "analytics-service",
    "notification-service",
    "enrichment-service"
]

base_dir = r"c:\Users\ashut\Devlopments\acquisition\acquisition"

for service in new_services:
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
        
    # Map service to its specific model
    model_import = "# no models yet"
    if service == "conversation-service":
        model_import = "from app.models.conversation import Conversation\nfrom app.models.message import Message"
    elif service == "analytics-service":
        model_import = "from app.models.event import Event"
    elif service == "notification-service":
        model_import = "from app.models.notification import Notification"
        
    env_content = env_content.replace(
        "target_metadata = None",
        f"import sys\nimport os\nsys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))\nfrom app.db.base import Base\n\n{model_import}\n\ntarget_metadata = Base.metadata"
    )
    
    with open(env_py_path, "w") as f:
        f.write(env_content)

print("Phase 2 Alembic Init Complete!")

import os
import subprocess
import sys

phase7_services = [
    "organization-service",
    "audit-service",
    "platform-api-service",
    "policy-service"
]

base_dir = os.path.dirname(os.path.abspath(__file__))

for service in phase7_services:
    print(f"\n--- Initializing Alembic for {service} ---")
    service_dir = os.path.join(base_dir, service)
    os.chdir(service_dir)
    
    # Initialize alembic if it doesn't exist
    if not os.path.exists("alembic"):
        subprocess.run([sys.executable, "-m", "alembic", "init", "alembic"])
    
    # modify alembic.ini to set version_table
    alembic_ini_path = "alembic.ini"
    if os.path.exists(alembic_ini_path):
        with open(alembic_ini_path, "r") as f:
            content = f.read()
        
        table_name = service.replace("-", "_") + "_alembic_version"
        if "# version_table = alembic_version" in content:
            content = content.replace("# version_table = alembic_version", f"version_table = {table_name}")
        
        content = content.replace("sqlalchemy.url = driver://user:pass@localhost/dbname", 'sqlalchemy.url = postgresql://postgres:postgres@localhost/acquisition')
        
        with open(alembic_ini_path, "w") as f:
            f.write(content)
            
        # modify env.py to import the models and set target_metadata
        env_py_path = "alembic/env.py"
        if os.path.exists(env_py_path):
            with open(env_py_path, "r") as f:
                env_content = f.read()
                
            # Map service to its specific model
            model_import = "# no models yet"
            if service == "organization-service":
                model_import = "from app.models.organization import Organization, OrganizationMember"
            elif service == "audit-service":
                model_import = "from app.models.audit import AuditLog"
            elif service == "platform-api-service":
                model_import = "from app.models.platform import APIKey, Webhook"
            elif service == "policy-service":
                model_import = "from app.models.policy import Policy"
                
            if "target_metadata = None" in env_content:
                env_content = env_content.replace(
                    "target_metadata = None",
                    f"import sys\nimport os\nsys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))\nfrom app.db.base import Base\n\n{model_import}\n\ntarget_metadata = Base.metadata"
                )
            
            with open(env_py_path, "w") as f:
                f.write(env_content)

print("\nPhase 7 Alembic Init Complete!")

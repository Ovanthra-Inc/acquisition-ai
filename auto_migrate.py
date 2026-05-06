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
    "notification-service",
    "deliverability-service",
    "security-service",
    "rate-limiting-service",
    "proxy-service",
    "observability-service",
    "optimization-service",
    "experimentation-service",
    "recommendation-service",
    "learning-service",
    "organization-service",
    "audit-service",
    "platform-api-service",
    "policy-service",
    "billing-service"
]

base_dir = os.path.dirname(os.path.abspath(__file__))

for service in services:
    print(f"\n--- Running migrations for {service} ---")
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

print("\n✅ All migrations complete.")

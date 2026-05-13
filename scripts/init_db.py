import os
import sys
from sqlalchemy import create_all, create_engine
from sqlalchemy.orm import declarative_base

# Add all service paths to sys.path to import their models
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICES = ["identity-service", "marketing-service", "intelligence-service", "comms-service", "ops-service"]

for service in SERVICES:
    sys.path.append(os.path.join(BASE_DIR, service))

def init_db():
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/acquisition")
    engine = create_engine(DATABASE_URL)
    
    print("Initializing Database Tables...")
    
    # We need to import all models so that SQLAlchemy knows about them
    # Since each service has its own Base, we need to create for each
    
    try:
        from identity_service.app.db.base import Base as IdentityBase
        IdentityBase.metadata.create_all(bind=engine)
        print("✓ Identity Service tables created.")
    except Exception as e:
        print(f"✗ Failed to init Identity Service: {e}")

    try:
        from marketing_service.app.db.base import Base as MarketingBase
        MarketingBase.metadata.create_all(bind=engine)
        print("✓ Marketing Service tables created.")
    except Exception as e:
        print(f"✗ Failed to init Marketing Service: {e}")

    try:
        from intelligence_service.app.db.base import Base as IntelligenceBase
        IntelligenceBase.metadata.create_all(bind=engine)
        print("✓ Intelligence Service tables created.")
    except Exception as e:
        print(f"✗ Failed to init Intelligence Service: {e}")

    try:
        from comms_service.app.db.base import Base as CommsBase
        CommsBase.metadata.create_all(bind=engine)
        print("✓ Comms Service tables created.")
    except Exception as e:
        print(f"✗ Failed to init Comms Service: {e}")

    try:
        from ops_service.app.db.base import Base as OpsBase
        OpsBase.metadata.create_all(bind=engine)
        print("✓ Ops Service tables created.")
    except Exception as e:
        print(f"✗ Failed to init Ops Service: {e}")

    print("\nDatabase initialization complete.")

if __name__ == "__main__":
    init_db()

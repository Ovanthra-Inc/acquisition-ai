from fastapi import APIRouter

router = APIRouter()

@router.post("/connect")
async def connect_source(source_type: str):
    return {"status": "connected", "source": source_type}

@router.post("/sync")
async def sync_source(source_type: str):
    return {"status": "syncing", "source": source_type}

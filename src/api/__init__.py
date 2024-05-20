from fastapi import APIRouter

from src.api.dependecies import get_api_key
from src.api.private import router as private
from src.api.public import router as public

router = APIRouter()
router.include_router(private)
router.include_router(public)


@router.get("/ping")
async def health_check() -> dict:
    return {"ping": "pong"}

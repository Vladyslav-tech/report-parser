from fastapi import APIRouter, Depends

from src.api.dependecies import get_api_key
from src.api.private.routes import router as partner_router

router = APIRouter(
    tags=['Private'],
    prefix='/private',
    dependencies=[Depends(get_api_key)]
)

router.include_router(partner_router)

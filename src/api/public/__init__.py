from fastapi import APIRouter, Depends

from src.api.dependecies import get_api_key
from src.api.public.routes import router as public_router

router = APIRouter(
    tags=['Public'],
    prefix='/public',
    dependencies=[Depends(get_api_key)]
)

router.include_router(public_router)

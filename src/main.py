import logging
from logging.config import dictConfig

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from src.api import router
from src.config.logger import logging_config

dictConfig(logging_config)
logger = logging.getLogger(__name__)


app = FastAPI()

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=['*'],
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")
from fastapi import Security
from fastapi.security.api_key import APIKeyHeader

from src.api.exceptions import ApiKeyException
from src.config.app import auth_settings

API_KEY = auth_settings.API_KEY
API_KEY_NAME = "Authorization"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)


async def get_api_key(api_key_header: str = Security(api_key_header)) -> str | None:
    if api_key_header == API_KEY:
        return api_key_header
    raise ApiKeyException

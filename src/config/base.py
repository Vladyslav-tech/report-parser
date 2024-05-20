from pydantic_settings import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    """Base settings."""
    model_config = {
        "extra": "allow",
        "env_file": "./src/.env",
    }

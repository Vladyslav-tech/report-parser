from src.config.integrations import BaseSettings


class AuthSettings(BaseSettings):
    """Auth settings."""
    API_KEY: str
    JWT_SECRET_KEY: str | None = None
    JWT_ALGORITHM: str | None = None


auth_settings = AuthSettings()

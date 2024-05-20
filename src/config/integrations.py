from src.config.base import BaseSettings


class GitHubSettings(BaseSettings):
    """GitHub settings."""
    GITHUB_HOST: str = "api.github.com"
    GITHUB_PROTOCOL: str = "https"
    GITHUB_TOKEN: str | None = None


github_settings = GitHubSettings()

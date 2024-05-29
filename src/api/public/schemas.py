from pydantic import BaseModel


class GitHubCheckRequest(BaseModel):
    """Check response schema."""
    owner: str
    repo: str
    path: str

    @property
    def endpoint(self):
        return f"repos/{self.owner}/{self.repo}/contents/{self.path}"

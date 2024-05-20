from fastapi import HTTPException, status


class ApiKeyException(HTTPException):
    def __init__(self) -> None:
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "Unauthorized"

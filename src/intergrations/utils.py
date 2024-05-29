from functools import wraps

from fastapi import HTTPException
from requests.exceptions import HTTPError


def override_api_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except HTTPError as err:
            raise HTTPException(status_code=err.response.status_code, detail=err.response.text)
    return wrapper

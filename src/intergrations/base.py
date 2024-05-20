from typing import Any, Dict, Protocol

import requests


class IApiClient(Protocol):
    """Interface for API clients."""
    def get(self, endpoint: str, params: Dict[str, Any] | None = None) -> requests.Response:
        raise NotImplementedError

    def post(self, endpoint: str, data: dict | None = None) -> requests.Response:
        raise NotImplementedError

    def put(self, endpoint: str, data: dict | None = None) -> requests.Response:
        raise NotImplementedError

    def delete(self, endpoint: str, data: dict | None = None) -> requests.Response:
        raise NotImplementedError


class ApiClient(IApiClient):
    def __init__(self,
                 protocol: str,
                 host: str,
                 token: str | None = None,
                 headers: Dict[str, str] | None = None):
        """Initialize the API client."""
        self.protocol = protocol
        self.host = host
        self.token = token
        self.headers = headers or {}

        if self.token:
            self.headers['Authorization'] = f'Bearer {self.token}'
        self.base_url = f"{self.protocol}://{self.host}"

    def get(self, endpoint: str, params: Dict[str, Any] | None = None) -> requests.Response:
        """Send a GET request to the specified endpoint."""
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response

    def post(self, endpoint: str, data: dict | None = None) -> requests.Response:
        """Send a POST request to the specified endpoint."""
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, headers=self.headers, data=data)
        response.raise_for_status()
        return response

    def put(self, endpoint: str, data: dict | None = None) -> requests.Response:
        """Send a PUT request to the specified endpoint."""
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, headers=self.headers, data=data)
        response.raise_for_status()
        return response

    def delete(self, endpoint: str, data: dict | None = None) -> requests.Response:
        """Send a DELETE request to the specified endpoint."""
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url, headers=self.headers, data=data)
        response.raise_for_status()
        return response

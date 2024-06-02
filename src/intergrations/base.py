from typing import Any, Dict, Protocol

import httpx


class IApiClient(Protocol):
    """Interface for API clients."""
    async def get(self, endpoint: str, params: Dict[str, Any] | None = None) -> httpx.Response:
        raise NotImplementedError

    async def post(self, endpoint: str, data: dict | None = None) -> httpx.Response:
        raise NotImplementedError

    async def put(self, endpoint: str, data: dict | None = None) -> httpx.Response:
        raise NotImplementedError

    async def delete(self, endpoint: str, data: dict | None = None) -> httpx.Response:
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

    async def get(self, endpoint: str, params: Dict[str, Any] | None = None) -> httpx.Response:
        """Send a GET request to the specified endpoint."""
        url = f"{self.base_url}/{endpoint}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers, params=params)

        return response

    async def post(self, endpoint: str, data: dict | None = None) -> httpx.Response:
        """Send a POST request to the specified endpoint."""
        url = f"{self.base_url}/{endpoint}"
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=self.headers, data=data)

        return response

    async def put(self, endpoint: str, data: dict | None = None) -> httpx.Response:
        """Send a PUT request to the specified endpoint."""
        url = f"{self.base_url}/{endpoint}"
        async with httpx.AsyncClient() as client:
            response = await client.put(url, headers=self.headers, data=data)

        return response

    async def delete(self, endpoint: str, data: dict | None = None) -> httpx.Response:
        """Send a DELETE request to the specified endpoint."""
        url = f"{self.base_url}/{endpoint}"
        async with httpx.AsyncClient() as client:
            response = await client.delete(url, headers=self.headers)

        return response

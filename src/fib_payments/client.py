from typing import Dict, Any, Optional
from .config import FIBConfig
from .exceptions import AuthenticationError, APIError
from .async_http_utils import HTTPClient


class FIBPaymentsClient:
    """Client for interacting with FIB Payments API."""

    def __init__(self, config: Optional[FIBConfig] = None):
        self.config = config or FIBConfig()
        self.config.validate()
        self.http_client = HTTPClient()
        self.token: Optional[str] = None

    async def _get_token(self) -> str:
        """Retrieve an access token."""
        if self.token:
            return self.token

        data = {
            'grant_type': 'client_credentials',
            'client_id': self.config.client_id,
            'client_secret': self.config.client_secret
        }

        response = await self.http_client.request('POST', self.config.auth_url, data=data)

        if response.status_code != 200:
            raise AuthenticationError(f"Failed to retrieve access token. Status: {response.status_code}")

        self.token = response.json()['access_token']
        return self.token

    async def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make an authenticated request to the API."""
        url = f"{self.config.api_url}{endpoint}"
        headers = {
            'Authorization': f"Bearer {await self._get_token()}",
            'Content-Type': 'application/json',
            'User-Agent': 'FIBPaymentsSDK',
        }
        kwargs['headers'] = headers

        response = await self.http_client.request(method, url, **kwargs)

        if response.status_code not in (200, 201):
            raise APIError(f"API request failed. Status: {response.status_code}, Body: {response.text}")

        return response.json()

    async def create_payment(self, amount: float, currency: Optional[str] = None,
                             callback_url: Optional[str] = None,
                             description: Optional[str] = None) -> Dict[str, Any]:
        """Create a new payment."""
        data = {
            'monetaryValue': {'amount': amount, 'currency': currency or self.config.currency},
            'statusCallbackUrl': callback_url or self.config.callback_url,
            'description': description or '',
            'refundableFor': self.config.refundable_for,
        }
        return await self._request('POST', '/payments', json=data)

    async def get_payment_status(self, payment_id: str) -> str:
        """Check the status of a payment."""
        response = await self._request('GET', f"/payments/{payment_id}/status")
        return response['status']

    async def refund_payment(self, payment_id: str) -> Dict[str, Any]:
        """Refund a payment."""
        return await self._request('POST', f"/payments/{payment_id}/refund")

    async def cancel_payment(self, payment_id: str) -> Dict[str, Any]:
        """Cancel a payment."""
        return await self._request('POST', f"/payments/{payment_id}/cancel")

    async def close(self):
        """Close the HTTP client."""
        await self.http_client.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

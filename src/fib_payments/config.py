import os
from dataclasses import dataclass


@dataclass
class FIBConfig:
    """Configuration for FIB Payments SDK."""
    base_url: str = os.getenv('FIB_BASE_URL', '')
    client_id: str = os.getenv('FIB_CLIENT_ID', '')
    client_secret: str = os.getenv('FIB_CLIENT_SECRET', '')
    callback_url: str = os.getenv('FIB_CALLBACK_URL', '')
    refundable_for: str = os.getenv('FIB_REFUNDABLE_FOR', 'P7D')
    currency: str = os.getenv('FIB_CURRENCY', 'IQD')

    @property
    def auth_url(self) -> str:
        return f"{self.base_url}/auth/realms/fib-online-shop/protocol/openid-connect/token"

    @property
    def api_url(self) -> str:
        return f"{self.base_url}/protected/v1"

    def validate(self):
        if not all([self.base_url, self.client_id, self.client_secret]):
            raise ValueError("Missing required configuration. "
                             "Please provide base_url, client_id, and client_secret.")

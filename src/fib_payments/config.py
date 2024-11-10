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
        missing_vars = [var for var in ['base_url', 'client_id', 'client_secret'] if not getattr(self, var)]
        if missing_vars:
            raise ValueError(f"Missing required configuration: {', '.join(missing_vars)}.")

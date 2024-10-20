class FIBPaymentsError(Exception):
    """Base exception for FIB Payments SDK."""


class ConfigurationError(FIBPaymentsError):
    """Raised when there's a configuration error."""


class AuthenticationError(FIBPaymentsError):
    """Raised when authentication fails."""


class APIError(FIBPaymentsError):
    """Raised when the API returns an error."""


class NetworkError(FIBPaymentsError):
    """Raised when there's a network-related error."""


class RetryExhaustedError(FIBPaymentsError):
    """Raised when all retry attempts have been exhausted."""

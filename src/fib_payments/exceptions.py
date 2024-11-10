class FIBPaymentsError(Exception):
    """Base exception for FIB Payments SDK."""

    def __init__(self, message: str = "An error occurred in FIB Payments SDK"):
        super().__init__(message)


class ConfigurationError(FIBPaymentsError):
    """Raised when there's a configuration error, such as missing required parameters."""

    def __init__(self, message: str = "Configuration error occurred."):
        super().__init__(message)


class AuthenticationError(FIBPaymentsError):
    """Raised when authentication fails due to invalid credentials or expired tokens."""

    def __init__(self, message: str = "Authentication failed."):
        super().__init__(message)


class APIError(FIBPaymentsError):
    """Raised when the API returns an error, indicating issues with the request or response."""

    def __init__(self, message: str = "API request failed."):
        super().__init__(message)


class NetworkError(FIBPaymentsError):
    """Raised when there's a network-related error, such as a timeout or connectivity issue."""

    def __init__(self, message: str = "Network error occurred."):
        super().__init__(message)


class RetryExhaustedError(FIBPaymentsError):
    """Raised when all retry attempts have been exhausted while trying to perform an operation."""

    def __init__(self, message: str = "All retry attempts have been exhausted."):
        super().__init__(message)

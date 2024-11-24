import asyncio
from functools import wraps
from typing import Any, Callable, Type
import httpx
from .exceptions import NetworkError, RetryExhaustedError


def async_retry(
        max_attempts: int = 3,
        delay: float = 0.1,
        max_delay: float = 10,
        backoff_factor: float = 2,
        exceptions: tuple = (httpx.NetworkError, httpx.TimeoutException)
) -> Callable:
    """
    Decorator for retrying asynchronous functions with exponential backoff.

    Args:
        max_attempts (int): Maximum number of retry attempts.
        delay (float): Initial delay between retries in seconds.
        max_delay (float): Maximum delay between retries in seconds.
        backoff_factor (float): Multiplicative factor for exponential backoff.
        exceptions (tuple): Exceptions to catch and retry on.

    Returns:
        Callable: Decorated function.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception: Exception | None = None
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt == max_attempts - 1:
                        raise RetryExhaustedError(f"Operation failed after {max_attempts} attempts: {str(e)}") from e

                    wait_time = min(delay * (backoff_factor ** attempt), max_delay)
                    await asyncio.sleep(wait_time)

            if last_exception:
                raise last_exception
            else:
                raise NetworkError("Retry function failed without catching any exceptions.")

        return wrapper

    return decorator


class HTTPClient:
    """Wrapper class for httpx.AsyncClient with built-in retry logic."""

    def __init__(self):
        self.client = httpx.AsyncClient()

    @async_retry()
    async def request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
        return await self.client.request(method, url, **kwargs)

    async def close(self):
        await self.client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: Any):
        await self.close()

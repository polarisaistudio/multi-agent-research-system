# src/tools/retry.py
import time
from functools import wraps
from typing import Callable

def retry_with_backoff(max_retries: int = 3, base_delay: float = 1.0):
    """Retry a function with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        return {"error": str(e), "retries": attempt + 1}

                    # Exponential backoff: 1s, 2s, 4s
                    delay = base_delay * (2 ** attempt)
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)

        return wrapper
    return decorator

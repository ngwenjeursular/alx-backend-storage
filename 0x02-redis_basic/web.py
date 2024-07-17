#!/usr/bin/env python3
"""
Web cache and tracker module
"""

import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()


def cache_with_expiry(expiration: int = 10) -> Callable:
    """
    Decorator to cache the result of a function with an expiry time.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            # Check if the URL's content is cached
            cached_content = r.get(url)
            if cached_content:
                return cached_content.decode('utf-8')

            # If not cached, call the function and cache the result
            result = func(url)
            r.setex(url, expiration, result)
            return result
        return wrapper
    return decorator


@cache_with_expiry(10)
def get_page(url: str) -> str:
    """
    Get the HTML content of a URL and track the access count.

    :param url: URL to fetch
    :return: HTML content of the URL
    """
    # Increment the access count for the URL
    count_key = f"count:{url}"
    r.incr(count_key)

    # Fetch the HTML content of the URL
    response = requests.get(url)
    return response.text

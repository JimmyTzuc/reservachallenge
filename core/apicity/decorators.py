from functools import wraps
from .utils import generate_cache_key, get_cache, set_cache
from django.conf import settings


def cache_decorator(key: str, complementary_keys=[], cache_ttl=settings.CACHE_TTL):
    """
    It caches the response of the decorated function:
    - `key` (required): main unique string.
    - `complementary_keys`: It expects a string array that matches the key_arguments
    of your decorated function.
    """

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            cache_key = generate_cache_key(key, complementary_keys, **kwargs)
            cached_result = get_cache(cache_key)

            if cached_result is None:
                cached_result = function(*args, **kwargs)
                set_cache(cache_key, cached_result, cache_ttl)

            return cached_result

        return wrapper

    return decorator

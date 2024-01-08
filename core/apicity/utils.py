from functools import reduce
from django.core.cache import cache
from django.conf import settings
import requests


def make_api_request(url, params, handle_429=False):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        if handle_429 and response.status_code == 429:
            return None

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error making request to API ({url}): {e}")
        return None


def generate_cache_key(key, complementary_keys, **kwargs):
    cache_key = key

    cache_key = (
        reduce(
            lambda acc, c_key: "{0}_{1}".format(acc, kwargs[c_key]),
            complementary_keys,
            cache_key,
        )
        .replace(" ", "_")
        .replace(",", "_")
    )

    return cache_key


def get_cache(cache_id):
    try:
        return cache.get(cache_id)
    except Exception:
        return None


def set_cache(cache_id, value, cache_ttl=settings.CACHE_TTL):
    cache.set(cache_id, value, cache_ttl)

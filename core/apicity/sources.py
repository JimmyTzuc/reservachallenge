from apicity.models import Key
from .decorators import cache_decorator
from .utils import make_api_request


def get_places(partial_name):
    return make_api_request(
        "https://search.reservamos.mx/api/v2/places",
        {
            "q": partial_name,
            "to": "ciudad-de-mexico"
        }
    )


@cache_decorator(key="weather_api", complementary_keys=["lat", "lon"])
def call_weather(lat, lon):
    apikey = Key.objects.get(name_service="weather").public_key
    return make_api_request(
        "https://api.openweathermap.org/data/2.5/onecall",
        {
            "lat": lat,
            "lon": lon,
            "appid": apikey,
            "units": "metric"
        },
        handle_429=True
    )


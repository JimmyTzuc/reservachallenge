import requests


def get_places(partial_name):
    url = "https://search.reservamos.mx/api/v2/places"
    params = {"q": partial_name, "to": "ciudad-de-mexico"}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        places = response.json()
        return places

    except requests.exceptions.RequestException as e:
        print(f"Error making request to Reservamos API: {e}")
        return None


def call_weather(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/onecall"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": "a5a47c18197737e8eeca634cd6acb581",
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        weather = response.json()
        return weather

    except requests.exceptions.RequestException as e:
        print(f"Error making request to Reservamos API: {e}")
        return None

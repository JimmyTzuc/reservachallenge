from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import call_weather, get_places


class GetCityForecast(APIView):
    def get(self, request, city_name):
        partial_name = city_name
        places_found = get_places(partial_name)

        if places_found:
            city_weather_info = []

            for item in places_found:
                if item["result_type"] == "city":
                    city_info = {
                        "display": item["display"],
                        "city_name": item["city_name"],
                        "state": item["state"],
                        "country": item["country"],
                        "lat": item["lat"],
                        "long": item["long"],
                        "result_type": item["result_type"],
                    }

                    lat = item["lat"]
                    lon = item["long"]

                    weather_found = call_weather(lat, lon)

                    daily = weather_found.get("daily", [])
                    city_weather_info.append(
                        {"city_info": city_info, "daily_forecast": daily}
                    )

            return Response({"found_cities": city_weather_info})
        else:
            return Response({"error": "No cities found."}, status=404)

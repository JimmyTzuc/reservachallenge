from .sources import call_weather, get_places
from .resolvers import sanitize_dt, sanitize_temp
from rest_framework.response import Response
from rest_framework.views import APIView


class GetCityForecast(APIView):
    def get(self, request, city_name):
        partial_name = city_name
        places_found = get_places(partial_name)

        if places_found:
            city_weather_info = []

            for item in places_found:
                if item["result_type"] == "city":
                    city_info = {
                        "id": item["id"],
                        "display": item["display"],
                        "city_name": item["city_name"],
                        "state": item["state"],
                        "country": item["country"],
                    }

                    lat = item["lat"]
                    lon = item["long"]

                    weather_found = call_weather(lat=lat, lon=lon)

                    daily = weather_found.get("daily", [])
                    daily_forecast = []
                    for forecast in daily:
                        dt = forecast["dt"]
                        formatted_date = sanitize_dt(dt)

                        day_temp = forecast["temp"]["day"]
                        formatted_day_temp = sanitize_temp(day_temp)

                        max_temp = forecast["temp"]["max"]
                        formatted_max_temp = sanitize_temp(max_temp)

                        min_temp = forecast["temp"]["min"]
                        formatted_min_temp = sanitize_temp(min_temp)

                        main_weather = forecast["weather"][0]["main"]

                        desc_weather = forecast["weather"][0]["description"]

                        icon_weather = forecast["weather"][0]["icon"]

                        forecast_info = {
                            "day": formatted_date,
                            "day_temp": formatted_day_temp,
                            "min_temp": formatted_min_temp,
                            "max_temp": formatted_max_temp,
                            "main_weather": main_weather,
                            "description_weather": desc_weather,
                            "icon_weather": icon_weather,
                        }
                        daily_forecast.append(forecast_info)
                    city_weather_info.append(
                        {"city_info": city_info, "daily_data": daily_forecast}
                    )

            return Response({"data": city_weather_info})
        else:
            return Response({"error": "No cities found."}, status=404)

from django.urls import path
from .views import GetCityForecast

urlpatterns = [
    path(
        "pronostico/<str:city_name>/",
        GetCityForecast.as_view(),
        name="pronostico_ciudad",
    ),
]

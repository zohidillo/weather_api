from django.urls import path
from rest_framework.routers import DefaultRouter

from src.apps.views import *

router = DefaultRouter()
router.register(r'weather', WeatherViewSet)

urlpatterns = [
                  path("weather/manual-update", ManualRefreshWeatherData.as_view())
              ] + router.urls

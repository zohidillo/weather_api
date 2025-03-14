import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.conf import settings

import src.core.models as models
import src.apps.serializers as serializers

API_KEY = settings.WEATHER_API


class ManualRefreshWeatherData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        the_last_datas = []
        for city in models.City.objects.all():
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={city.latitude}&lon={city.longitude}&appid={API_KEY}&units=metric"

            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                data = response.json()

                obj = models.Weather.objects.create(
                    city=city,
                    temperature=data["main"]["temp"],
                    humidity=data["main"]["humidity"],
                    pressure=data["main"]["pressure"],
                    wind_speed=data["wind"]["speed"],
                    weather_description=data["weather"][0]["description"]
                )
                the_last_datas.append(obj)
            except requests.RequestException as e:
                print(f"❌ Xatolik: {e}")
                continue
        data = serializers.WeatherSerializer(the_last_datas, many=True).data
        return Response(data)

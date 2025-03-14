import requests
from celery import shared_task
from django.conf import settings

import src.core.models as models

API_KEY = settings.WEATHER_API


@shared_task
def fetch_weather_data():
    """OpenWeatherMap API dan ob-havo ma’lumotlarini olib, bazaga saqlaydi"""
    for city in models.City.objects.all():
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={city.latitude}&lon={city.longitude}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            models.Weather.objects.create(
                city=city,
                temperature=data["main"]["temp"],
                humidity=data["main"]["humidity"],
                pressure=data["main"]["pressure"],
                wind_speed=data["wind"]["speed"],
                weather_description=data["weather"][0]["description"]
            )
        except requests.RequestException as e:
            print(f"❌ Xatolik: {e}")
            continue
    return "Weather data updated successfully"

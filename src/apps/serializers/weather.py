from src.apps.serializers.base import *

import src.shared as shared
import src.core.models as models


class WeatherSerializer(BaseSerializer):
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=models.City.objects.all(), source="city", write_only=True
    )
    city = serializers.SerializerMethodField()

    class Meta:
        model = models.Weather
        fields = ["id", "city_id", "city", "temperature", "humidity", "pressure", "wind_speed", "weather_description",
                  "added_at"]
        extra_kwargs = {
            'added_at': {'read_only': True}
        }

    def get_city(self, obj):
        return {
            "id": obj.city.id,
            "name": obj.city.name,
            "latitude": obj.city.latitude,
            "longitude": obj.city.longitude
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["weather_description"] = shared.translate_weather(instance.weather_description)
        return data

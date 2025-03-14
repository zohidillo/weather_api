from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from drf_yasg.utils import swagger_auto_schema

import src.shared as shared
import src.core.models as models
import src.apps.serializers as serializer


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = models.Weather.objects.select_related("city")
    serializer_class = serializer.WeatherSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        "city": ["exact"],
        "added_at": ["exact", "gte", "lte"]
    }
    search_fields = ["city__name"]

    @swagger_auto_schema(manual_parameters=shared.filter_weather_data())
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

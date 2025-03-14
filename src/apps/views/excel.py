from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
from django.utils.dateparse import parse_datetime

import src.shared as shared
import src.core.models as models
import src.apps.serializers as serializers


class GenerateFileData(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(manual_parameters=shared.filter_weather_data(True))
    def get(self, request):
        qs = models.Weather.objects.select_related("city")
        city = self.request.query_params.get("city", None)
        search = self.request.query_params.get("search", None)
        added_at__gte = self.request.query_params.get("added_at__gte", None)
        added_at__lte = self.request.query_params.get("added_at__lte", None)
        file_type = request.query_params.get("file_type", "xlsx")

        if city:
            qs = qs.filter(city_id=city)
        if search:
            qs = qs.filter(city__name=search)

        if added_at__gte:
            qs = qs.filter(added_at__gte=added_at__gte)

        if added_at__lte:
            qs = qs.filter(added_at__lte=added_at__lte)

        data = serializers.WeatherSerializer(qs, many=True).data
        if file_type == "csv":
            return shared.generate_csv(data)
        return shared.generate_excel(data)

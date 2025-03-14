from django.contrib import admin

import src.core.models as models


@admin.register(models.Weather)
class WeatherApiAdmin(admin.ModelAdmin):
    ...

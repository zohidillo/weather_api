from django.urls import path, include

urlpatterns = [
    path("", include("src.apps.urls.weather")),
    path("file", include("src.apps.urls.file")),
]

from django.urls import path

from src.apps.views import GenerateFileData

urlpatterns = [
    path("", GenerateFileData.as_view())
]

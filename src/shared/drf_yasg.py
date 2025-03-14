from drf_yasg import openapi
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view

API_TITLE = 'API doc'
API_DESCRIPTION = 'API documents'

yasg_schema_view = get_schema_view(
    openapi.Info(
        title=API_TITLE,
        default_version='v1',
        description=API_DESCRIPTION,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="example@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

admin.site.site_title = "Admin panel"
admin.site.site_header = "Admin panel"
admin.site.index_title = "Admin panel"

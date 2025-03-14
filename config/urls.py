from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from src.shared.drf_yasg import yasg_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('src.api.include_routers')),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', yasg_schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', yasg_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

import debug_toolbar

urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="API Restaurantes & Reviews",
        default_version='v1',
        description="Documentación API completa para Restaurantes y Reviews",
    ),
    validators=['flex'],  # permite validaciones adicionales
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # App Restaurante
    path('api/', include('review.urls')),
    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Sirve archivos multimedia durante desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

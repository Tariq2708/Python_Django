# codemonk/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Define schema view for Swagger and ReDoc
schema_view = get_schema_view(
    openapi.Info(
        title="Codemonk API",  # Title of the API
        default_version='v1',  # API version
        description="API documentation for Codemonk project",  # Description of the API
        terms_of_service="https://www.example.com/policies/terms/",  # Terms of service URL
        contact=openapi.Contact(email="contact@example.com"),  # Contact email
        license=openapi.License(name="MIT License"),  # License information
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Permissions for accessing the documentation
)

# URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site path
    path('api/', include('rest.urls')),  # Include URLs from the rest app
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI documentation
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc documentation
]

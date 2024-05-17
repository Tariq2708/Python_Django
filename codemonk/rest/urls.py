from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    CustomUserListCreateAPIView, 
    CustomUserRetrieveUpdateDestroyAPIView, 
    save_paragraph, 
    search_paragraph
)

# Define URL patterns for the API endpoints
urlpatterns = [
    # Endpoint for creating and listing users
    path('users/', CustomUserListCreateAPIView.as_view(), name='user-list-create'),

    # Endpoint for retrieving, updating, and deleting a specific user by ID
    path('users/<int:pk>/', CustomUserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),

    # Endpoint for obtaining JWT token pair
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Endpoint for refreshing JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Endpoint for saving paragraphs
    path('api/save-paragraph/', save_paragraph, name='save_paragraph'),

    # Endpoint for searching within paragraphs
    path('api/search/', search_paragraph, name='search'),

    # Alias for the search endpoint (optional, can be removed if redundant)
    path('api/search-paragraph/', search_paragraph, name='search_paragraph'),
]

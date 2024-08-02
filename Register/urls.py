from django.urls import path
from .views import user_registration_api_view

urlpatterns = [
    path('auth/register/', user_registration_api_view)
]

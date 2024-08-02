from django.urls import path
from .views import user_profile_info_api_view
urlpatterns = [
    path('profile/', user_profile_info_api_view)
]

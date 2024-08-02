from django.urls import path
from .views import InternalFlightListGenericApiView
urlpatterns = [
    path('internal-flights/', InternalFlightListGenericApiView.as_view())
]

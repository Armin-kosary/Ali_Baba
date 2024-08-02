from django.urls import path
from .views import InternationalFlightListGenericApiView
urlpatterns = [
    path('international-flights/', InternationalFlightListGenericApiView.as_view())
]

from django.shortcuts import render
from rest_framework import generics
from .models import InternationalFlight
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import InternationalFlightSerializer
from .filters import InternationalFlightsListFilter
# Create your views here.


class InternationalFlightListGenericApiView(generics.ListAPIView):
    queryset = InternationalFlight.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = InternationalFlightSerializer
    filterset_class = InternationalFlightsListFilter
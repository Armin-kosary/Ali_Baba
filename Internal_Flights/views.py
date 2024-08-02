from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.request import Request
from .models import InternalFlight
from rest_framework.response import Response
from .serializers import InternalFlightSerializer
from django_filters import rest_framework as filter
from .models import InternalFlight
from django_filters.rest_framework import DjangoFilterBackend
from .filters import InternalFlightsListFilter
# Create your views here.

class InternalFlightListGenericApiView(generics.ListAPIView):
    queryset = InternalFlight.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = InternalFlightSerializer
    filterset_class = InternalFlightsListFilter
    # permission_classes = [IsAdminUser]
    # authentication_classes = [TokenAuthentication]
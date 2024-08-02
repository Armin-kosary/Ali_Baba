from rest_framework import serializers
from .models import InternalFlight


class InternalFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalFlight
        fields = ["starting_point", "destination", "ticket_type", "departure_date", "return_date", "passengers", "price"]
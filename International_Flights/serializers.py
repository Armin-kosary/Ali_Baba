from rest_framework import serializers
from .models import InternationalFlight

class InternationalFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalFlight
        fields = ["starting_point", "destination", "ticket_type", "departure_date", "return_date", "passengers", "price"]
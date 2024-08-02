from django_filters import rest_framework as filter
from .models import InternalFlight


class InternalFlightsListFilter(filter.FilterSet):
    min_price = filter.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filter.NumberFilter(field_name='price', lookup_expr='lte')
    class Meta:
        model = InternalFlight
        fields = ["starting_point", "destination", "ticket_type", "departure_date", "return_date", "passengers"]

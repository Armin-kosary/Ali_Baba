from django_filters import rest_framework as filter
from .models import InternationalFlight


class InternationalFlightsListFilter(filter.FilterSet):
    min_price = filter.NumberFilter(field_name="price", lookup_expr="lte")
    max_price = filter.NumberFilter(field_name="price", lookup_expr="gte")
    class Meta:
        model = InternationalFlight
        fields = ["starting_point", "destination", "ticket_type", "departure_date", "return_date", "passengers", "price"]

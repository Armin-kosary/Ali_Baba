from django.db import models

# Create your models here.


class InternalFlight(models.Model):
    ticket_type = (
        ("ONE-WAY", "One Way"),
        ("ROUND-TRIP", "Round Trip"),
    )
    starting_point = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    ticket_type = models.CharField(max_length=50, choices=ticket_type)
    departure_date = models.CharField(max_length=50)
    return_date = models.CharField(max_length=50)
    passengers = models.CharField(max_length=10)
    price = models.PositiveIntegerField(null=True)
from django.db import models


class Flight(models.Model):
    SOUTHWEST = 'SWA'
    AMERICAN = 'AAL'
    UNITED = 'UAL'
    DELTA = 'DAL'
    JETBLUE = 'JBU'
    AIRLINE_CHOICES = (
        (SOUTHWEST, 'Southwest'),
        (AMERICAN, 'American'),
        (UNITED, 'United'),
        (DELTA, 'Delta'),
        (JETBLUE, 'JetBlue'),
    )
    airline = models.CharField(max_length=3,
                               choices=AIRLINE_CHOICES,
                               default=SOUTHWEST)
    number = models.CharField(max_length=10)

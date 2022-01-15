from django.db import models

from .constants import CHANNEL, COUNTRY, OS


class Metrics(models.Model):
    date = models.DateField()
    channel = models.CharField(choices=CHANNEL, max_length=16)
    country = models.CharField(choices=COUNTRY, max_length=2)
    os = models.CharField(choices=OS, max_length=7)
    impressions = models.PositiveIntegerField()
    clicks = models.PositiveIntegerField()
    installs = models.PositiveIntegerField()
    spend = models.DecimalField(max_digits=8, decimal_places=3)
    revenue = models.DecimalField(max_digits=8, decimal_places=3)

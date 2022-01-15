from django_filters import rest_framework as filters

from .models import Metrics


class MetricsFilter(filters.FilterSet):
    class Meta:
        model = Metrics
        fields = ['date']

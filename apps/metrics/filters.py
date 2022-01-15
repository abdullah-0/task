from django_filters import rest_framework as filters, ChoiceFilter, DateFilter

from .constants import CHANNEL, COUNTRY, OS
from .models import Metrics


class MetricsFilter(filters.FilterSet):
    channel = ChoiceFilter(choices=CHANNEL)
    country = ChoiceFilter(choices=COUNTRY)
    os = ChoiceFilter(choices=OS)
    date_from = DateFilter(field_name='date', lookup_expr='gte')
    date_to = DateFilter(field_name='date', lookup_expr='lte')
    date_before = DateFilter(field_name='date', lookup_expr='lt')
    date_after = DateFilter(field_name='date', lookup_expr='gt')

    class Meta:
        model = Metrics
        fields = ['channel', 'country', 'os', 'date', 'date_from', 'date_to', 'date_before', 'date_after']

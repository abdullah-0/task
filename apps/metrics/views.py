import pandas as pd
from django.db.models import ExpressionWrapper, F, FloatField
from rest_framework import generics, status
from rest_framework.response import Response

from .filters import MetricsFilter
from .models import Metrics
from .serializers import MetricsSerializer


class MetricsListView(generics.ListCreateAPIView):
    queryset = Metrics.objects.all(). \
        annotate(cpi=ExpressionWrapper(F('spend') / F('installs'), output_field=FloatField()))
    serializer_class = MetricsSerializer
    filterset_class = MetricsFilter

    def get_queryset(self):
        qs = self.queryset
        if len(self.request.query_params) > 0:
            order_by = self.request.query_params.get('order_by') if self.request.query_params.get('order_by') else 'id'
            order = '-' if self.request.query_params.get('order') == 'des' else ''
            qs = self.queryset.order_by(order + order_by)
        return qs

    def post(self, request, *args, **kwargs):
        if request.FILES.get('file'):
            try:
                csv = pd.read_csv(request.FILES.get('file')).T.to_dict()
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            data = []
            for row in csv.items():
                data.append(
                    Metrics(date=row[1]['date'],
                            channel=row[1]['channel'],
                            country=row[1]['country'],
                            os=row[1]['os'],
                            impressions=row[1]['impressions'],
                            clicks=row[1]['clicks'],
                            installs=row[1]['installs'],
                            spend=row[1]['spend'],
                            revenue=row[1]['revenue']
                            ))
            Metrics.objects.bulk_create(data, batch_size=100)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

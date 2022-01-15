import pandas as pd
from rest_framework import generics, status
from rest_framework.response import Response

from .filters import MetricsFilter
from .models import Metrics
from .serializers import MetricsSerializer


class MetricsListView(generics.ListCreateAPIView):
    queryset = Metrics.objects.all()
    serializer_class = MetricsSerializer
    filterset_class = MetricsFilter

    def post(self, request, *args, **kwargs):
        if request.FILES.get('file'):
            csv = pd.read_csv(request.FILES.get('file')).T.to_dict()
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

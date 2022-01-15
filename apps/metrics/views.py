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
        return Response(status=status.HTTP_201_CREATED)

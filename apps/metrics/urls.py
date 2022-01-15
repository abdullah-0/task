from django.urls import path

from apps.metrics.views import MetricsListView

urlpatterns = [
    path('metrics/', MetricsListView.as_view())
]

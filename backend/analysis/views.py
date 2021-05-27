from rest_framework import serializers, viewsets, permissions

from analysis.models import Analysis
from analysis.serializers import AnalysisSerializer


class AnalysisViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]

    queryset = Analysis.objects.all().order_by("-id")
    serializer_class = AnalysisSerializer

from analysis.models import Analysis
from rest_framework import serializers, viewsets
from analysis.serializers import AnalysisSerializer


class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer

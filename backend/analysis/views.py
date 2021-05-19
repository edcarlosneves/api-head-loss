from analysis.models import Analysis, PipeMaterial
from rest_framework import serializers, viewsets
from analysis.serializers import AnalysisSerializer, PipeMaterialSerializer


class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer


class PipeMaterialViewSet(viewsets.ModelViewSet):
    queryset = PipeMaterial.objects.all()
    serializer_class = PipeMaterialSerializer

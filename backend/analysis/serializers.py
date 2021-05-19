from rest_framework import serializers

from analysis.models import Analysis, PipeMaterial


class AnalysisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Analysis
        fields = "__all__"


class PipeMaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PipeMaterial
        fields = "__all__"

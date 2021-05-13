from rest_framework import serializers
from rest_framework.utils import field_mapping

from analysis.models import Analysis


class AnalysisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Analysis
        fields = ["analysis_name"]

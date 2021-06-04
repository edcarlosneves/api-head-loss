from rest_framework import serializers, validators

from analysis.models import Analysis
from .utils import (
    calculate_head_loss,
    calculate_reynolds_number,
    get_reynolds_number_regime,
)


class AnalysisSerializer(serializers.ModelSerializer):
    # head_loss = serializers.FloatField(read_only=True)
    # reynolds_number = serializers.FloatField(read_only=True)
    # reynolds_number_regime = serializers.CharField(read_only=True)
    test_calculated_value = serializers.SerializerMethodField()

    # def create(self, validated_data):
    #     try:
    #         reynolds_number = calculate_reynolds_number(
    #             validated_data["pipe_diameter"],
    #             validated_data["kinematic_viscosity"],
    #             validated_data["volumetric_flow_rate"],
    #         )
    #         reynolds_number_regime = get_reynolds_number_regime(reynolds_number)
    #     except ValueError:
    #         raise serializers.ValidationError(
    #             {
    #                 "reynolds_number": "The values you entered do not match a valid analysis."
    #             }
    #         )
    #
    #     try:
    #         head_loss = calculate_head_loss(
    #             validated_data["pipe_length"],
    #             validated_data["pipe_diameter"],
    #             validated_data["kinematic_viscosity"],
    #             validated_data["volumetric_flow_rate"],
    #             validated_data["pipe_material"],
    #             validated_data["material_condition"],
    #         )
    #     except ValueError:
    #         raise serializers.ValidationError(
    #             {"head_loss": "The values you entered do not match a valid analysis."}
    #         )
    #
    #     analysis = Analysis.objects.create(**validated_data)
    #     analysis.head_loss = head_loss
    #     analysis.reynolds_number = reynolds_number
    #     analysis.reynolds_number_regime = reynolds_number_regime
    #     analysis.save()
    #
    #     return analysis

    class Meta:
        model = Analysis
        fields = "__all__"

    def get_test_calculated_value(self, obj):
        return 1.365 - obj.volumetric_flow_rate

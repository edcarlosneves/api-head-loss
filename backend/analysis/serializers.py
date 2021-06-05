from rest_framework import serializers, validators

from .models import Analysis
from .utils import (
    calculate_head_loss,
    calculate_reynolds_number,
    get_reynolds_number_regime,
    AVERAGE_ROUGHNESS_DATA,
)


class AnalysisSerializer(serializers.ModelSerializer):

    head_loss = serializers.SerializerMethodField()
    reynolds_number = serializers.SerializerMethodField()
    reynolds_number_regime = serializers.SerializerMethodField()

    def create(self, validated_data):
        if validated_data["pipe_material"] not in AVERAGE_ROUGHNESS_DATA.keys():
            raise serializers.ValidationError(
                {
                    "pipe_material": "The material you entered do not match a valid material."
                }
            )

        if (
            validated_data["material_condition"]
            not in AVERAGE_ROUGHNESS_DATA[validated_data["pipe_material"]].keys()
        ):
            raise serializers.ValidationError(
                {
                    "material_condition": "The material_condition you entered do not match a valid material_condition."
                }
            )
        analysis = Analysis.objects.create(**validated_data)

        analysis.save()
        return analysis

    class Meta:
        model = Analysis
        fields = "__all__"

    def get_head_loss(self, obj):
        try:
            head_loss = calculate_head_loss(
                obj.pipe_length,
                obj.pipe_diameter,
                obj.kinematic_viscosity,
                obj.volumetric_flow_rate,
                obj.pipe_material,
                obj.material_condition,
            )
        except ValueError:
            raise serializers.ValidationError(
                {"head_loss": "The values you entered do not match a valid analysis."}
            )
        return head_loss

    def get_reynolds_number(self, obj):
        try:
            reynolds_number = calculate_reynolds_number(
                obj.pipe_diameter,
                obj.kinematic_viscosity,
                obj.volumetric_flow_rate,
            )
        except ValueError:
            raise serializers.ValidationError(
                {
                    "reynolds_number": "The values you entered do not match a valid analysis."
                }
            )
        return reynolds_number

    def get_reynolds_number_regime(self, obj):
        try:
            reynolds_number = calculate_reynolds_number(
                obj.pipe_diameter,
                obj.kinematic_viscosity,
                obj.volumetric_flow_rate,
            )
        except ValueError:
            raise serializers.ValidationError(
                {
                    "reynolds_number_regime": "The values you entered do not match a valid analysis."
                }
            )
        reynolds_number_regime = get_reynolds_number_regime(reynolds_number)
        return reynolds_number_regime

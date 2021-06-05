from django.db import models
from django.core.exceptions import ValidationError
from math import pi, log10
from scipy import constants

from .managers import TurbulentRegimeManager


class Analysis(models.Model):
    def validate_positive_float(value):
        if value <= 0.0:
            raise ValidationError(
                ("%(value)s must be in greater than 0."),
                params={"value": value},
            )

    analysis_name = models.CharField("analysis name", max_length=255)
    density = models.FloatField("density", validators=[validate_positive_float])
    kinematic_viscosity = models.FloatField(
        "kinematic viscosity", validators=[validate_positive_float]
    )
    pipe_diameter = models.FloatField(
        "pipe diameter", validators=[validate_positive_float]
    )
    volumetric_flow_rate = models.FloatField(
        "volumetric flow rate", validators=[validate_positive_float]
    )
    pipe_material = models.CharField("pipe material", max_length=255)
    material_condition = models.CharField("material condition", max_length=255)
    pipe_length = models.FloatField("pipe length", validators=[validate_positive_float])
    owner = models.ForeignKey(
        "accounts.UserProfile", related_name="analyses", on_delete=models.CASCADE
    )

    objects = models.Manager()
    turbulent_regime_objects = TurbulentRegimeManager()

    def __str__(self):
        return f"{self.analysis_name} - {self.owner}"

    class Meta:
        verbose_name_plural = "Analyses"

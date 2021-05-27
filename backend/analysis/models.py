from django.db import models
from math import pi, log10
from scipy import constants

from .utils import calculate_head_loss


class Analysis(models.Model):

    analysis_name = models.CharField("analysis name", unique=True, max_length=255)
    density = models.FloatField("density")
    kinematic_viscosity = models.FloatField("kinematic viscosity")
    pipe_diameter = models.FloatField("pipe diameter")
    volumetric_flow_rate = models.FloatField("volumetric flow rate")
    pipe_material = models.CharField("pipe material", max_length=255)
    material_condition = models.CharField("material condition", max_length=255)
    pipe_length = models.FloatField("pipe length")
    head_loss = models.FloatField("head loss", null=True, blank=True)
    owner = models.ForeignKey(
        "accounts.User", related_name="analyses", on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        self.head_loss = calculate_head_loss(
            self.pipe_length,
            self.pipe_diameter,
            self.kinematic_viscosity,
            self.volumetric_flow_rate,
            self.pipe_material,
            self.material_condition,
        )
        super(Analysis, self).save(*args, **kwargs)
        return self.head_loss

    def __str__(self):
        return f"{self.analysis_name} - [{self.pk}]"

    class Meta:
        verbose_name_plural = "Analyses"

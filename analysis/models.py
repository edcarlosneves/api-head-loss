from django.db import models


class PipeMaterial(models.Model):
    material = models.CharField(max_length=255)

    def __str__(self):
        return self.material


class Analysis(models.Model):
    analysis_name = models.CharField(max_length=255)
    density = models.FloatField(null=True, blank=True)
    kinematic_viscosity = models.FloatField(null=True, blank=True)
    pipe_diameter = models.FloatField(null=True, blank=True)
    volumetric_flow_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.analysis_name} - [{self.pk}]"

    class Meta:
        verbose_name_plural = "Analyses"

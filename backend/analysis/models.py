from django.db import models
from math import pi, log10
from scipy import constants


class PipeMaterial(models.Model):
    material = models.CharField(max_length=255)

    def __str__(self):
        return self.material


class Analysis(models.Model):
    AVERAGE_ROUGHNESS = {
        "steel": {
            "sheet_metal_new": {"ft": 1.6e-4, "m": 5.0e-2},
            "stainless_new": {"ft": 7.0e-6, "m": 2.0e-3},
            "commercial_new": {"ft": 1.50e-4, "m": 4.60e-2},
            "riveted": {"ft": 1.0e-2, "m": 3.0},
            "rusted": {"ft": 7.0e-3, "m": 2.0},
        },
        "iron": {
            "cast_new": {"ft": 8.50e-4, "m": 2.60e-1},
            "wrought_new": {"ft": 1.50e-4, "m": 4.60e-2},
            "galvanized_new": {"ft": 5.0e-4, "m": 1.50e-1},
            "asphalted_cast": {"ft": 4.00e-4, "m": 1.20e-1},
        },
        "brass": {"drawn_new": {"ft": 7.0e-6, "m": 2.0e-3}},
        "plastic": {"drawn_tubing": {"ft": 5.0e-6, "m": 1.50e-3}},
        "glass": {"not_applicable": {"ft": 0, "m": 0}},
        "concrete": {
            "smoothed": {"ft": 1.30e-4, "m": 4.0e-2},
            "rough": {"ft": 7.00e-3, "m": 2.0},
        },
        "rubber": {"smoothed": {"ft": 3.30e-5, "m": 1.0e-2}},
        "wood": {"stave": {"ft": 1.60e-3, "m": 5.0e-1}},
    }

    analysis_name = models.CharField("analysis name", unique=True, max_length=255)
    density = models.FloatField("density")
    kinematic_viscosity = models.FloatField("kinematic viscosity")
    pipe_diameter = models.FloatField("pipe diameter")
    volumetric_flow_rate = models.FloatField("volumetric flow rate")
    pipe_material = models.CharField("pipe material", max_length=255)
    material_condition = models.CharField("material condition", max_length=255)
    pipe_length = models.FloatField("pipe length")
    head_loss = models.FloatField("head loss", null=True, blank=True)

    # @staticmethod
    # def _validate_field_value(field):
    #     if not field:
    #         raise ValueError("pipe_diameter is not defined...")

    def _calculate_cross_sectional_area(self):
        # self._validate_field_value(self.pipe_diameter)
        return (self.pipe_diameter ** 2) * (pi / 4)

    def _calculate_fluid_velocity(self):
        _area = self._calculate_cross_sectional_area()
        return self.volumetric_flow_rate / _area

    def _calculate_reynolds_number(self):
        _flud_velocity = self._calculate_fluid_velocity()
        return (self.pipe_diameter * _flud_velocity) / self.kinematic_viscosity

    @staticmethod
    def _get_reynolds_number_regime(reynolds_number):
        if reynolds_number < 2300:
            return "laminar"
        elif reynolds_number > 2600:
            return "turbulent"
        else:
            return "transitional"

    def _calculate_average_roughness(self):
        return self.AVERAGE_ROUGHNESS[self.pipe_material][self.material_condition]["m"]

    def _calculate_relative_roughness(self):
        _average_roughness = self._calculate_average_roughness()
        return _average_roughness / self.pipe_diameter

    def _calculate_friction_factor(self):
        _relative_roughness = self._calculate_average_roughness()
        _reynolds_number = self._calculate_reynolds_number()
        _equation_p1 = -4 * log10(
            (_relative_roughness / 3.7)
            - (5.02 / _reynolds_number)
            * log10((_relative_roughness / 3.7) + (13 / _reynolds_number))
        )
        return 1 / (_equation_p1 ** 2)

    def _calculate_head_loss(self):
        _fluid_velocity = self._calculate_fluid_velocity()
        _friction_factor = self._calculate_friction_factor()
        return (
            2
            * _friction_factor
            * (self.pipe_length / self.pipe_diameter)
            * ((_fluid_velocity ** 2) / constants.g)
        )

    def save(self, *args, **kwargs):
        self.head_loss = self._calculate_head_loss()
        super(Analysis, self).save(*args, **kwargs)
        return self.head_loss

    def __str__(self):
        return f"{self.analysis_name} - [{self.pk}]"

    class Meta:
        verbose_name_plural = "Analyses"

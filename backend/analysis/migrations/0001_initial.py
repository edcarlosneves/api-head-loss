# Generated by Django 3.2.2 on 2021-06-04 01:51

import analysis.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Analysis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "analysis_name",
                    models.CharField(max_length=255, verbose_name="analysis name"),
                ),
                (
                    "density",
                    models.FloatField(
                        validators=[analysis.models.Analysis.validate_positive_float],
                        verbose_name="density",
                    ),
                ),
                (
                    "kinematic_viscosity",
                    models.FloatField(
                        validators=[analysis.models.Analysis.validate_positive_float],
                        verbose_name="kinematic viscosity",
                    ),
                ),
                (
                    "pipe_diameter",
                    models.FloatField(
                        validators=[analysis.models.Analysis.validate_positive_float],
                        verbose_name="pipe diameter",
                    ),
                ),
                (
                    "volumetric_flow_rate",
                    models.FloatField(
                        validators=[analysis.models.Analysis.validate_positive_float],
                        verbose_name="volumetric flow rate",
                    ),
                ),
                (
                    "pipe_material",
                    models.CharField(max_length=255, verbose_name="pipe material"),
                ),
                (
                    "material_condition",
                    models.CharField(max_length=255, verbose_name="material condition"),
                ),
                (
                    "pipe_length",
                    models.FloatField(
                        validators=[analysis.models.Analysis.validate_positive_float],
                        verbose_name="pipe length",
                    ),
                ),
                (
                    "head_loss",
                    models.FloatField(blank=True, null=True, verbose_name="head loss"),
                ),
                (
                    "reynolds_number",
                    models.FloatField(
                        blank=True, null=True, verbose_name="reynolds number"
                    ),
                ),
                (
                    "reynolds_number_regime",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        null=True,
                        verbose_name="reynolds number regime",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Analyses",
            },
        ),
    ]

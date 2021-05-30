# Generated by Django 3.2.2 on 2021-05-20 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analysis", "0006_auto_20210520_0212"),
    ]

    operations = [
        migrations.AlterField(
            model_name="analysis",
            name="analysis_name",
            field=models.CharField(max_length=255, verbose_name="Analysis Name"),
        ),
        migrations.AlterField(
            model_name="analysis",
            name="density",
            field=models.FloatField(blank=True, null=True, verbose_name="Density"),
        ),
        migrations.AlterField(
            model_name="analysis",
            name="head_loss",
            field=models.FloatField(blank=True, null=True, verbose_name="Head Loss"),
        ),
        migrations.AlterField(
            model_name="analysis",
            name="kinematic_viscosity",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Kinematic Viscosity"
            ),
        ),
        migrations.AlterField(
            model_name="analysis",
            name="material_condition",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Material Condition"
            ),
        ),
        migrations.AlterField(
            model_name="analysis",
            name="pipe_diameter",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Pipe Diameter"
            ),
        ),
        migrations.AlterField(
            model_name="analysis",
            name="pipe_length",
            field=models.FloatField(blank=True, null=True, verbose_name="Pipe Length"),
        ),
        migrations.AlterField(
            model_name="analysis",
            name="pipe_material",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Pipe Material"
            ),
        ),
        migrations.AlterField(
            model_name="analysis",
            name="volumetric_flow_rate",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Volumetric Flow Rate"
            ),
        ),
    ]
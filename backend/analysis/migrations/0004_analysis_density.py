# Generated by Django 3.2.2 on 2021-05-13 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analysis", "0003_rename_analisys_analysis"),
    ]

    operations = [
        migrations.AddField(
            model_name="analysis",
            name="density",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.2.2 on 2021-05-27 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("analysis", "0011_delete_pipematerial"),
    ]

    operations = [
        migrations.AddField(
            model_name="analysis",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="analyses",
                to="accounts.user",
            ),
            preserve_default=False,
        ),
    ]

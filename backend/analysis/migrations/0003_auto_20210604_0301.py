# Generated by Django 3.2.2 on 2021-06-04 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_analysis_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysis',
            name='head_loss',
        ),
        migrations.RemoveField(
            model_name='analysis',
            name='reynolds_number',
        ),
        migrations.RemoveField(
            model_name='analysis',
            name='reynolds_number_regime',
        ),
    ]

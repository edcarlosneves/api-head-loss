from django.db import models


class Analysis(models.Model):
    analysis_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Analyses"

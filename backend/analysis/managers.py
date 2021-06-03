from django.db import models


class TurbulentRegimeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(reynolds_number_regime="turbulent")

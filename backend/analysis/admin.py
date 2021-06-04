from django.contrib import admin
from analysis.models import Analysis


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from analysis.models import Analysis


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    readonly_fields = ("head_loss",)

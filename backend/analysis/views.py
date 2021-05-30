from django.contrib import auth
from rest_framework import viewsets, permissions, authentication

from analysis.models import Analysis
from analysis.serializers import AnalysisSerializer


class AnalysisViewSet(viewsets.ModelViewSet):
    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Analysis.objects.all().order_by("-id")
    serializer_class = AnalysisSerializer

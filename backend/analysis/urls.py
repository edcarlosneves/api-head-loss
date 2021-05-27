from django.urls import include, path
from rest_framework import routers, urlpatterns
from analysis import views

router = routers.DefaultRouter()
router.register(r"analysis", views.AnalysisViewSet)

urlpatterns = [path("", include(router.urls))]

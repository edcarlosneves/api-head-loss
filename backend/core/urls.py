from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/", include("analysis.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include("web_interface.urls")),
]

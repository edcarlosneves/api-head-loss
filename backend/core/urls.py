from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from accounts.views import CustomAuthToken

urlpatterns = [
    path("api-token-auth/", CustomAuthToken.as_view()),
    path("analysis/", include("analysis.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("user-profile/", include("accounts.urls")),
]

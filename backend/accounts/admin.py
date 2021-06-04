from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import UserProfile


class UserProfileAdmin(BaseUserAdmin):
    ordering = ("email",)
    model = UserProfile

    list_display = ("email", "name", "is_active", "is_staff", "is_superuser")

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "name",
                    "password",
                )
            },
        ),
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "password",
                )
            },
        ),
    )


admin.site.register(UserProfile, UserProfileAdmin)

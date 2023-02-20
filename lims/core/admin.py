from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [ 'username', 'email']
    list_display_links = ['username']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "photo",
            "telephone")
        }),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
        }),
        ("Password change information", {
            "fields": (
                "secret_question",
                "secret_answer"
            )
        }),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_active", "is_superuser")

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ["username", "email", "is_staff", "is_active", "is_superuser"]


admin.site.register(CustomUser, CustomUserAdmin)

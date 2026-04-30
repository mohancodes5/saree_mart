from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Store", {"fields": ("is_vendor", "phone")}),
    )
    list_display = ("username", "email", "is_vendor", "is_staff", "is_superuser")

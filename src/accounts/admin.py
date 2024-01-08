from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


@admin.register(get_user_model())
class CustomerAdmin(UserAdmin):
    ordering = ("email",)
    list_display = ("email", "first_name", "last_name")
    fieldsets = None
    readonly_fields = ("email",)

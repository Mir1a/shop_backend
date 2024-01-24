from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "name", "last_name", "is_active"]
    fields = ["email", "name", "last_name", "password"]



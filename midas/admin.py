from django.contrib import admin
from .models import User

from finance.admin import TransactionInLine
from product.admin import OrderInLine


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "name", "last_name", "is_active"]
    fields = ["email", "name", "last_name", "password", "favorites"]
    inlines = [TransactionInLine, OrderInLine]

    def get_queryset(self, request):
        queryset = super(UserAdmin, self)\
            .get_queryset(request)

        return queryset.prefetch_related("favorites")
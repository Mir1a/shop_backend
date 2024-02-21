from django.contrib import admin
from django.db import models

from .models import Transaction
from midas.models import User


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["code", "price", "status", "order", "user", "real_name"]
    readonly_fields = ["code", "price"]

    def get_queryset(self, request):
        queryset = super(TransactionAdmin, self) \
            .get_queryset(request)

        return queryset\
            .select_related("user")\
            .annotate(real_name=\
                User.objects\
                    .filter(id=models.OuterRef("user"))\
                    .values("name")
            )

    @admin.display(description="Real",
                   ordering='real_name')
    def real_name(self, instance):
        return instance.real_name

class TransactionInLine(admin.TabularInline):
    model = Transaction

class UserAdmin(admin.ModelAdmin):
    inlines = [
        TransactionInLine
    ]

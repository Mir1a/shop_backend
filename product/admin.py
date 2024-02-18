from django.contrib import admin
from django.db import models

from midas.models import User
from .models import Item
from .models import Order
from .models import Supply

admin.site.register(Item)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user_email", "status", "sum_price", "amount_items"]
    readonly_fields = ["sum_price", "amount_items"]

    def get_queryset(self, request):
        queryset = super(OrderAdmin, self) \
            .get_queryset(request)

        return queryset\
            .select_related("user")\
            .prefetch_related("items")\
            .annotate(user_email=\
                User.objects\
                    .filter(id=models.OuterRef("user"))\
                    .values("email")
            )

    @admin.display(description="Пользователь",
                   ordering='user_email')
    def user_email(self, instance):
        return instance.user_email


admin.site.register(Supply)
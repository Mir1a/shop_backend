from django.contrib import admin
from .models import Item
from .models import Order
from .models import Supply

admin.site.register(Item)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
        list_display = ["id", "user", "status", "sum_price", "amount_items"]
        readonly_fields = ["sum_price", "amount_items"]


admin.site.register(Supply)
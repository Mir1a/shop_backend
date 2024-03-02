from django.contrib import admin
from django.db import models

from midas.models import User
from .models import Item
from .models import Order
from .models import Supply
from .models import Supply_sender

#ForeignKey простой
class OrderInLine(admin.TabularInline):
    model = Order
#ManytoManymodel'
class MtMOrder_and_Item(admin.TabularInline):
    model = Order.items.through

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "code", "color", "weight", "height", "width", "double_buy"]
    inlines = [MtMOrder_and_Item]
    def get_queryset(self, request):
        queryset = (super(ItemAdmin, self)
                    .get_queryset(request))
        return queryset\
    .annotate\
            (double_buy=models.F("price") * 2)

    @admin.display(description="double",
                   ordering='double_buy')
    def double_buy(self, instance):
        return instance.double_buy

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user_email", "status", "sum_price", "amount_items", "sum_with_discount"]
    readonly_fields = ["sum_price", "amount_items", "status"]
    inlines = [MtMOrder_and_Item]
    def get_queryset(self, request):
        queryset = super(OrderAdmin, self) \
            .get_queryset(request)
        return queryset\
            .select_related("user")\
            .prefetch_related("items")\
            .annotate(user_email=\
                User.objects\
                    .filter(id=models.OuterRef("user"))\
                    .values("email")) \
            .annotate(sum_with_discount=models.Sum("items__price") - (
            models.Sum(models.F("items__price") * models.F("discount") / 100)))

    @admin.display(description="Пользователь",
                   ordering='user_email')
    def user_email(self, instance):
        return instance.user_email
    @admin.display(description="Цена со скидкой",
                   ordering='sum_with_discount')
    def sum_with_discount(self, instance):
        formatted_sum = '{:.2f}'.format(instance.sum_with_discount) #не забыть {} :-начало формата, .2 - к-во знаков после запятой, f - формат float
        return formatted_sum





admin.site.register(Supply)
admin.site.register(Supply_sender)
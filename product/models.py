from django.db import models
from django.core import validators
from . import choices
from multiselectfield import MultiSelectField


class Item(models.Model):
    title = models.TextField(max_length=500,  null=False, blank=False)
    description = models.TextField(max_length=1000, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validators.MinValueValidator(1)])
    code = models.IntegerField(unique=True, null=False, blank=False)
    color = models.CharField(max_length=20)
    weight = models.DecimalField(max_digits=10, decimal_places=1)
    height = models.DecimalField(max_digits=10, decimal_places=1)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    types = MultiSelectField(max_length=10, choices=choices.type_choices, null=True, blank=True, default=1)
    amount = models.IntegerField(null=True, blank=False, default=0)

    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"

    def __str__(self):
        return self.title


class Order(models.Model):
    # region           -----Information-----
    sum_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amount_items = models.PositiveIntegerField(null=True, blank=True)
    status = models.IntegerField(choices=choices.order_statuses, default=1)
    discount = models.IntegerField(null=True, blank=True, default=0)
    # endregion

    # region           -----Relation-----
    user = models.ForeignKey(to="midas.User", on_delete=models.CASCADE)
    items = models.ManyToManyField(to="product.Item", related_name="orders")
    # endregion
    class Meta:
        verbose_name_plural = "Заказы"
        verbose_name = "Заказ"

    def __str__(self):
        return str(self.id)


class Supply(models.Model):
    data = models.FileField(upload_to='uploads/')
    class Meta:
        verbose_name_plural = "Поставки"
        verbose_name = "Поставка"

    def __str__(self):
        return str(self.id)

class Supply_sender(models.Model):
    item = models.ManyToManyField(to="product.Item", related_name="supply_sender")
    amount = models.IntegerField(null=False, blank=False)
    code = models.IntegerField(unique=True, null=True, blank=True)
    class Meta:
        verbose_name_plural = "Поставки на отправление"
        verbose_name = "Поставка на отправление"

    def __str__(self):
        return str(self.code)
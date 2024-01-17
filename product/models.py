from django.db import models
from django.core import validators
from . import choices


class Item(models.Model):
    title = models.TextField(max_length=500,  null=False, blank=False)
    description = models.TextField(max_length=1000, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validators.MinValueValidator(1)])
    code = models.IntegerField(unique=True, null=False, blank=False)
    color = models.CharField(max_length=20)
    weight = models.DecimalField(max_digits=10, decimal_places=1)
    height = models.DecimalField(max_digits=10, decimal_places=1)
    width = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Order(models.Model):
    # region           -----Information-----
    sum_price = models.DecimalField(max_digits=10, decimal_places=2)
    amount_items = models.PositiveIntegerField()
    # TODO сделать через choices
    status = models.IntegerField(choices=choices.order_statuses)
    # endregion

    # region           -----Relation-----
    user = models.ForeignKey(to="midas.User", on_delete=models.CASCADE)
    items = models.ManyToManyField(to="product.Item")
    # endregion

    def __str__(self):
        return str(self.id)


class Supply(models.Model):
    data = models.JSONField()

    def __str__(self):
        return str(self.id)
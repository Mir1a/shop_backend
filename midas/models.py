from django.db import models
from django.utils import timezone
from . import choices
from django.core import validators
# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=False, blank=False)
    avatar = models.ImageField(upload_to='users/avatar', null=True, blank=True)
    born = models.DateField(default=timezone.now, null=True, blank=True)
    favorites = models.ManyToManyField(to="midas.Item")

    def __str__(self):
        return self.id


class Transaction(models.Model):
    code = models.CharField(max_length=50)
    user = models.ForeignKey(to="midas.User", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255, choices=choices.statuses)
    order = models.OneToOneField(to="midas.Order", on_delete=models.CASCADE)

    def __str__(self):
        return self.id


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
    items = models.ManyToManyField(to="midas.Item")
    # endregion

    def __str__(self):
        return self.id


class Supply(models.Model):
    data = models.JSONField()

    def __str__(self):
        return self.id
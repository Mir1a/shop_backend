from django.db import models
from . import choices
from django.utils import timezone


class Transaction(models.Model):
    code = models.CharField(max_length=50)
    user = models.ForeignKey(to="midas.User", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default="1")
    status = models.CharField(max_length=255, choices=choices.statuses)
    order = models.OneToOneField(to="product.Order", on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name_plural = "Транзакции"
        verbose_name = "Транзакция"

    def __str__(self):
        return str(self.code)
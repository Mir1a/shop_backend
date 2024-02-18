# region				-----External Imports-----
from django.db.models import signals, OuterRef, Count, Sum, Subquery
from django import dispatch
import typing
from finance.models import Transaction
# endregion

# region				-----Internal Imports-----
from ... import models
# endregion

# region			  -----Supporting Variables-----
# endregion


@dispatch.receiver(signals.m2m_changed, sender=models.Order.items.through)
def order_calculation_init(sender, instance, action, *args: typing.List,
                           **kwargs: typing.Dict) -> None:
    if action in ["post_add", "post_remove"]:
        result = instance.items\
            .all()\
            .aggregate(Count("id"), Sum("price"))

        models.Order.objects\
            .filter(id=instance.id)\
            .update(amount_items=result.get("id__count"),
                    sum_price=result.get("price__sum"))

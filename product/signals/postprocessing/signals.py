#region -----Library import-----
from django.db.models.signals import post_save
from django.dispatch import receiver
import openpyxl
#endregion
#region -----Local import-----
from product.models import Supply
from product.models import Item
#endregion

@receiver(post_save, sender=Supply)
def update_item_amount(sender, instance, created, **kwargs):
    if created:
        wb = openpyxl.load_workbook(instance.data)
        sheet = wb.active
        for row in sheet.iter_rows(values_only=True):
            item_name = row[0]
            amount = row[1]
            try:
                item = Item.objects.get(title=item_name.strip())
                item.amount += amount
                item.save()
            except Item.DoesNotExist:
                pass
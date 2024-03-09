#region -----Library import-----
from rest_framework import serializers
#endregion

#region -----Local import-----
from product.models import Item
from product.models import Order
from product.models import Supply_sender
from product.models import Supply
#endregion
#region -----ItemSerializer-----
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "title")
# "title", "description", "price", "code", "color", "weight", "height", "width
#endregion
#region -----OrderSerializer-----
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "sum_price")
# "amount_items", "status", "user", "items"
#endregion
#region -----Supply_senderSerializer-----
class Supply_senderSerializer(serializers.ModelSerializer):
    item_names = serializers.SerializerMethodField()
    class Meta:
        model = Supply_sender
        fields = ("id", "item_names", "amount",)

    def get_item_names(self, instance):
        items = instance.item.all()
        item_names = ', '.join(
            [item.title for item in items])
        return item_names
#endregion
#region -----SupplySerializer-----
class SupplySerializer(serializers.ModelSerializer):
    data = serializers.FileField(required=True, use_url=True)

    class Meta:
        model = Supply
        fields = ("data", )
#endregion
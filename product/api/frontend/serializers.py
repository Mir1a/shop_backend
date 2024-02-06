# region				-----External Imports-----
from product.api.general import serializers as product_serializers
# endregion

# region				-----Internal Imports-----
from ..general import serializers as general_serializers
from ... import models as product_models
# endregion

#region                               Item serializer
class ItemSerializerTake(general_serializers.ItemSerializer):
    class Meta(general_serializers.ItemSerializer.Meta):
        fields = general_serializers.ItemSerializer.Meta.fields + ("description", "price", "code", "color", "weight", "height", "width")

class ItemSerializerAll(general_serializers.ItemSerializer):
    class Meta(general_serializers.ItemSerializer.Meta):
        fields = general_serializers.ItemSerializer.Meta.fields\
                 + ("price", "description")
#endregion

#region order serializers
class OrderSerializerTake(general_serializers.OrderSerializer):
    class Meta(general_serializers.OrderSerializer.Meta):
        fields = general_serializers.OrderSerializer.Meta.fields + ("status", "amount_items", "user", "items")

class OrderSerializerAll(general_serializers.OrderSerializer):
    class Meta(general_serializers.OrderSerializer.Meta):
        fields = general_serializers.OrderSerializer.Meta.fields + ("status", "amount_items")

#endregion
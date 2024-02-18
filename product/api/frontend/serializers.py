# region				-----External Imports-----
from product.api.general import serializers as product_serializers
from rest_framework import serializers
from midas.api.frontend.serializers import ReadUserSerializer
from midas import models as midas_models
# endregion

# region				-----Internal Imports-----
from ..general import serializers as general_serializers
from ... import models as product_models
from ... import choices as product_choices
# endregion

#region                               Item serializer
class ItemSerializerTake(general_serializers.ItemSerializer):
    class Meta(general_serializers.ItemSerializer.Meta):
        fields = general_serializers.ItemSerializer.Meta.fields + ("description", "price", "code", "color", "weight", "height", "width", "types")


class ItemSerializerAll(general_serializers.ItemSerializer):
    class Meta(general_serializers.ItemSerializer.Meta):
        fields = general_serializers.ItemSerializer.Meta.fields\
                 + ("price", "description")
#endregion

#region order serializers
class OrderSerializerTake(general_serializers.OrderSerializer):
    items = ItemSerializerTake(many=True)
    user = ReadUserSerializer(many=False)

    class Meta(general_serializers.OrderSerializer.Meta):
        fields = general_serializers.OrderSerializer.Meta.fields + ("status", "amount_items", "user", "items")


class OrderSerializerAll(general_serializers.OrderSerializer):
    Total_sum = serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta(general_serializers.OrderSerializer.Meta):
        fields = general_serializers.OrderSerializer.Meta.fields + ("status", "amount_items", "Total_sum")


class OrderSerializerCreate(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=midas_models.User.objects.all(),
                                              default=serializers.CurrentUserDefault())

    class Meta:
        model = product_models.Order
        fields = ("user", "items")
#endregion
from rest_framework import serializers
from product.models import Item
from product.models import Order


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "title")
# "title", "description", "price", "code", "color", "weight", "height", "width


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "sum_price")
# "amount_items", "status", "user", "items"


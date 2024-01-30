from rest_framework import serializers
from product.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "title", "description", "price", "code", "color", "weight", "height", "width")

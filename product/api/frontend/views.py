from rest_framework import viewsets, mixins, renderers, permissions as rest_permissions
from django import shortcuts
from ..general import serializers
from . import permissions
from product.models import Item

class ItemViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin):
    serializer_class = serializers.ItemSerializer
    queryset = Item.objects.all()
    permission_classes = []

from rest_framework import viewsets, mixins as rest_mixins, renderers, permissions as rest_permissions
from django import shortcuts
from ..general import serializers as product_general_serializer
from . import permissions
from . import serializers
from product.models import Item
from product.models import Order
from utils import mixins as utils_mixins


class ItemViewSet(utils_mixins.DynamicSerializersViewSet,
                  utils_mixins.PrefetchableRetrieveMixin,
                  utils_mixins.PrefetchableListMixin):

    default_serializer_class = product_general_serializer.ItemSerializer
    serializer_classes = {"list": serializers.ItemSerializerAll,
                          "retrieve": serializers.ItemSerializerTake}
    permission_classes = []

    # region -----Default Parameters-----
    queryset = Item.objects
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = []
    # endregion
    def _prefetch_list(self, queryset):
        return queryset\
            .only("id", "title", "price", "description")


class OrderViewSet(utils_mixins.DynamicSerializersViewSet,
                  utils_mixins.PrefetchableRetrieveMixin,
                  utils_mixins.PrefetchableListMixin,):
    default_serializer_class = product_general_serializer.OrderSerializer
    serializer_classes = {"list": serializers.OrderSerializerAll,
                          "retrieve": serializers.OrderSerializerTake}

    queryset = Order.objects
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = []

    def _prefetch_list(self, queryset):
        return queryset\
            .only("id", "sum_price", "status", "amount_items")

from rest_framework import filters as rest_filters, mixins as rest_mixins, renderers, permissions as rest_permissions
from django import shortcuts
from ..general import serializers as product_general_serializer
from django_filters import rest_framework as filters
from . import permissions
from . import serializers
from product.models import Item
from product.models import Order
from utils import mixins as utils_mixins
from utils.third_party.api.rest_framework import paginators as utils_paginators

from . import filters as product_filters


class ItemViewSet(utils_mixins.DynamicSerializersViewSet,
                  utils_mixins.PrefetchableRetrieveMixin,
                  utils_mixins.PrefetchableListMixin):

    default_serializer_class = product_general_serializer.ItemSerializer
    serializer_classes = {"list": serializers.ItemSerializerAll,
                          "retrieve": serializers.ItemSerializerTake}
    permission_classes = []

    # region -----Default Parameters-----
    pagination_class = utils_paginators.StandartPagePaginator
    queryset = Item.objects
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = []
    # endregion

    # region		  -----Filters and Sortings-----
    filter_backends = [product_filters.ItemFilterBackend,
                       rest_filters.OrderingFilter,
                       filters.DjangoFilterBackend]
    filterset_class = product_filters.ItemFilterSet
    ordering_fields = ["title", "id", "price"]
    ordering = ["-price"]
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

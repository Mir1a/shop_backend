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
from django.db.models import Sum

#region -----ItemViewSet-----
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
#endregion
#region -----OrderViewSet-----
class OrderViewSet(utils_mixins.DynamicSerializersViewSet,
                   utils_mixins.PrefetchableRetrieveMixin,
                   utils_mixins.PrefetchableListMixin,
                   rest_mixins.CreateModelMixin):
    default_serializer_class = product_general_serializer.OrderSerializer
    serializer_classes = {"list": serializers.OrderSerializerAll,
                          "retrieve": serializers.OrderSerializerTake,
                          "create": serializers.OrderSerializerCreate}

    queryset = Order.objects.prefetch_related("items").annotate(Total_sum=Sum("items__price"))
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [rest_permissions.IsAuthenticated]
    pagination_class = utils_paginators.StandartPagePaginator

    #region sort and filters
    filter_backends = [product_filters.OrderFilterBackend,
                       rest_filters.OrderingFilter,
                       filters.DjangoFilterBackend]
    filterset_class = product_filters.OrderFilterSet
    ordering_fields = ["id", "sum_price"]
    ordering = ["id"]
    #endregion

    def _prefetch_list(self, queryset):
        return queryset\
            .prefetch_related("items")\
            .select_related("user")\
            .only("id", "sum_price", "status", "amount_items", "user", "items")
#endregion

#region -----Library Import-----
from rest_framework import filters as rest_filters, mixins as rest_mixins, renderers, permissions as rest_permissions
from django import shortcuts
from django_filters import rest_framework as filters
from django.db.models import Sum
import pandas as pd
import io
from django.http import HttpResponse
from rest_framework import permissions as rest_permissions
#endregion

#region -----Local Import-----
from . import permissions
from . import serializers
from . import filters as product_filters
from ..general import serializers as product_general_serializer
from product.models import Item
from product.models import Order
from product.models import Supply_sender
from utils import mixins as utils_mixins
from utils.third_party.api.rest_framework import paginators as utils_paginators
#endregion



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
#region -----Supply_senderViewSet-----
class Supply_senderViewSet(utils_mixins.PrefetchableListMixin):
    serializer_class = product_general_serializer.Supply_senderSerializer
    permission_classes = [rest_permissions.AllowAny]
    queryset = Supply_sender.objects

    def list(self, request, *args, **kwargs):
        # region -----ViewSet_settings-----
        queryset = self.queryset
        serializer = self.get_serializer(queryset, many=True)
        # endregion

        data = serializer.data
        df = pd.DataFrame(data)

        excel_file = io.BytesIO()

        df.to_excel(excel_file, index=False)

        excel_file.seek(0)

        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="transaction_data.xlsx"'
        return response
#endregion
#region -----SupplyViewSet-----
from rest_framework import viewsets, status
from rest_framework.response import Response
import pandas as pd
from product.models import Item, Supply_sender, Supply
from ..general import serializers
from rest_framework.parsers import MultiPartParser, FormParser

class SupplyViewSet(viewsets.ViewSet):

    serializer_class = serializers.SupplySerializer
    queryset = Supply.objects
    permission_classes = [rest_permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, pk=None):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'No file received'}, status=status.HTTP_400_BAD_REQUEST)


#endregion
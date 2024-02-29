# region				-----External Imports-----
from rest_framework import viewsets, mixins, renderers, permissions, generics
from django import shortcuts
from utils import mixins as utils_mixins
from ..general import serializers as finance_general_serializer
# endregion

# region				-----Internal Imports-----
from ...models import Transaction
# endregion

class TransactionViewSet(utils_mixins.DynamicSerializersViewSet,
                         utils_mixins.PrefetchableListMixin):
    default_serializer_class = finance_general_serializer.TransactionSerializer
    # region -----Default Parameters-----
    queryset = Transaction.objects
    permission_classes = [permissions.IsAdminUser]
    # endregion


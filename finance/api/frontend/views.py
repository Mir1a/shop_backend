from rest_framework import viewsets, mixins, renderers, permissions, generics
from django import shortcuts
from django.db import models
import pandas as pd
from django.http import HttpResponse

from utils import mixins as utils_mixins
from ..general import serializers as finance_general_serializer
from ...models import Transaction
import io
from midas.models import User

class TransactionViewSet(utils_mixins.DynamicSerializersViewSet,
                         utils_mixins.PrefetchableListMixin):
    default_serializer_class = finance_general_serializer.TransactionSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Transaction.objects.filter(status='1').select_related("user").annotate(email=models.F('user__email'))

    def list(self, request, *args, **kwargs):
        queryset = Transaction.objects.filter(status='1').select_related("user").annotate(create_at_annotation=models.F('create_at'), email=models.F('user__email'))
        serializer = self.default_serializer_class(queryset, many=True)
        data = serializer.data
        df = pd.DataFrame(data)


        excel_file = io.BytesIO()

        df.to_excel(excel_file, index=False)

        excel_file.seek(0)

        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="transaction_data.xlsx"'
        return response
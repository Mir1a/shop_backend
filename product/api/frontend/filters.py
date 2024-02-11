# region				-----External Imports-----
from django import http
from django.db import models
from rest_framework import views, filters as rest_filters
from django_filters import rest_framework as filters
# endregion

#region ItemFilterBackend
class ItemFilterBackend(rest_filters.BaseFilterBackend):
    def filter_queryset(self, request: http.HttpRequest,
                        queryset: models.QuerySet,
                        view: views.APIView)\
            -> models.QuerySet:
        return queryset.filter(price__lte=200)
#endregion

#region ItemFilterSet
class ItemFilterSet(filters.FilterSet):
      title = filters.CharFilter(field_name="title",
                                 lookup_expr="icontains")

      price = filters.NumberFilter(field_name="price",
                                  lookup_expr="icontains")

      price__gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
#endregion

#region OrderFilterBackend
class OrderFilterBackend(rest_filters.BaseFilterBackend):
    def filter_queryset(self, request: http.HttpRequest,
                        queryset: models.QuerySet,
                        view: views.APIView)\
            -> models.QuerySet:
        return queryset.filter(sum_price__gte=0)
#endregion

#region ItemFilterSet

class OrderFilterSet(filters.FilterSet):
    filter_sum_price_lte = filters.CharFilter(field_name="sum_price",
                               lookup_expr="lte")

    filter_amount_items_gte = filters.NumberFilter(field_name="amount_items",
                                 lookup_expr="gte")

    filter_sum_price_gt = filters.NumberFilter(field_name='sum_price', lookup_expr='gt')
#endregion
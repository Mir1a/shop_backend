# region				-----External Imports-----
from django import http
from django.db import models
from rest_framework import views, filters as rest_filters
from django_filters import rest_framework as filters
# endregion


class ItemFilterBackend(rest_filters.BaseFilterBackend):
    def filter_queryset(self, request: http.HttpRequest,
                        queryset: models.QuerySet,
                        view: views.APIView)\
            -> models.QuerySet:
        return queryset.filter(price__lte=200)


class ItemFilterSet(filters.FilterSet):
      title = filters.CharFilter(field_name="title",
                                 lookup_expr="icontains")

      price = filters.NumberFilter(field_name="price",
                                  lookup_expr="icontains")

      price__gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
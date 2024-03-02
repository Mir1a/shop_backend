from rest_framework import serializers
from finance.models import Transaction
from midas.models import User
from django.db import models


class TransactionSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user__email', read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'price', 'user', 'status', 'order', 'email', 'create_at')

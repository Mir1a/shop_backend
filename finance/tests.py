

from midas.models import User
from .models import Transaction
from product.models import Order, Item
# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

class TransactionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(email="testuser@gmail.com", password="password")
        self.item = Item.objects.create(title="Test Item", description="Test Description", price=10.00, code=123456, color="Red", weight=10.0, height=5.0, width=2.5, amount=5)
        self.order = Order.objects.create(status=1, user=self.user)
        self.order.items.add(self.item)
        self.transaction = Transaction.objects.create(code="1", user=self.user, price="1", status=1, order=self.order)
        self.client = APIClient()

        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_transaction_list(self):
        url = reverse("transaction-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.contrib.messages.storage.fallback import FallbackStorage
from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.http import HttpResponse


from midas.models import User
from product.admin import ItemAdmin
from product.models import Item

#region ItemAdminTest
# class ItemAdminTest(TestCase):
#     serialized_rollback = True
#
#     def setUp(self):
#         self.item = Item.objects.create(
#             title= 'Test Item',
#             description= 'Test Description',
#             price= 10.00,
#             code= 123456,
#             color= 'Red',
#             weight= 1.5,
#             height= 10.0,
#             width= 5.5,
#             types= ["КБТ", "МБТ"],
#             amount= 5,)
#         self.client = Client()
#         self.user = User.objects.create_superuser(email='admin@example.com', password='admin')
#     #region unwork test
#     # def test_create_item_admin(self):
#     #     self.client.login(email='admin@example.com', password='admin')
#     #     #Это удалить и ничего не измениться
#     #     create_form_url = reverse(
#     #         f"admin:product_item_add")
#     #     response = self.client.post(create_form_url, {
#     #         'title': 'Test Item',
#     #         'description': 'Test Description',
#     #         'price': 10.00,
#     #         'code': 123456,
#     #         'color': 'Red',
#     #         'weight': 1.5,
#     #         'height': 10.0,
#     #         'width': 5.5,
#     #         'types': ["КБТ", "МБТ"],
#     #         'amount': 5,
#     #     })
#     #
#     #     #self.assertEqual(response.status_code, 302)
#     #     self.assertTrue(Item.objects.filter(title='Test Item').exists())
#     #endregion
#     #region Тест на адрес рабочий
#     # def test_admin_url(self):
#     #     admin_url = reverse('admin:index')
#     #     self.assertEqual(admin_url, '/admin/')
#     #endregion
#     #region Тест на создание итема без админки
#     # def test_create_item(self):
#     #     item = Item.objects.create(name="Example Item", description="Example Description", price=10.0)
#     #     self.assertIsNotNone(item)
#     #endregion
#     def test_create_item(self):
#         def test_create_item(self):
#             Item.objects.create(
#             title= 'Test Item',
#             description= 'Test Description',
#             price= -10.00,
#             code= 123456,
#             color= 'Red',
#             weight= "sdaf",
#             height= 10.0,
#             width= 5.5,
#             types= ["КБТ", "МБТ"],
#             amount= 5,)
#
#
#             self.assertEqual(Item.objects.filter(title="Test Item").count(), 1)
#endregion

#region -----ItemApiTest-----
class ItemTests(APITestCase):
    def setUp(self):
        self.item_data = {
            "title": "Test Item",
            "description": "Test Description",
            "price": 10.00,
            "code": 123456,
            "color": "Red",
            "weight": 10.0,
            "height": 5.0,
            "width": 2.5,
            "types": ["КБТ", "МБТ"],
            "amount": 5,
        }
        #** - распаковывают json в набор value
        Item.objects.create(**self.item_data)

    #рабочий тест
    def test_get_item_list(self):
        #routers?
        url = reverse("item-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    #не рабочий тест
    def test_create_item(self):
        url = reverse("item-list")
        new_item_data = {
            "title": "New Test Item",
            "description": "New Test Description",
            "price": 20.00,
            "code": 654321,
            "color": "Blue",
            "weight": 15.0,
            "height": 7.0,
            "width": 3.5,
            "types": ["КБТ", "МБТ"],
            "amount": 10,
        }
        #наверное тут ломается потому что нет возможности post в листе
        response = self.client.post(url, new_item_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #рабочий тест
    def test_get_item_detail(self):
        item = Item.objects.first()
        url = reverse("item-detail", args=[item.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
#endregion

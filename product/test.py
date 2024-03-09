# region				-----External Imports-----
from midas import models as user_models
from django import test
from http import HTTPStatus
from django.urls import reverse
from django.conf import settings
# endregion
# endregion

# region				-----Internal Imports-----

from .models import Item
# endregion

# region			  -----Supporting Variables-----
# endregion

class ItemTestMixin(test.TestCase):
    client = test.Client()
    def setUp(self) -> None:
        self.item = Item.objects.create(
            title="item_title_1",
            description="item_description_1",
            price=-10.00,
            code=123456,
            color="Red",
            weight=1.5,
            height=10.0,
            width=5.5,
            types=["КБТ", "МБТ"],
            amount=5
        )

        self.user = user_models.User.objects\
            .create_superuser(email="admin@gmail.com",
                              name="admin",
                              password="admin")

        self.client.login(email='admin@gmail.com',
                          password='admin')


class ItemAdminTest(ItemTestMixin):
    def test_item_create(self):
        create_form_url = reverse("admin:product_item_add")

        response = self.client.post(
            create_form_url, data={"title":"item_title_1",
            "description":"item_description_1",
            "price":10.00,
            "code":123456,
            "color":"Red",
            "weight":1.5,
            "height":10.0,
            "width":5.5,
            "types":["КБТ", "МБТ"],
            "amount":5}
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_item_update(self):
        item = Item.objects.first()
        change_form_url = reverse(
            "admin:product_item_change", args=[item.pk]
        )

        response = self.client.post(
            change_form_url, data={
                "title": "New title",
                "description": "New description",
            }, follow=True
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_item_changelist(self):
        change_list_url = reverse("admin:product_item_changelist")
        response = self.client.get(change_list_url, follow=True)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_item_delete(self):
        item = Item.objects.first()
        delete_form_url = reverse(
            "admin:product_item_delete", args=[item.pk]
        )

        response = self.client.post(delete_form_url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

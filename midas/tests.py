# from django.test import TestCase
# from django import test
#
# from .models import User
# # Create your tests here.
# class UserTestMixin(test.TestCase):
#     client = test.Client()
#
#     def setUp(self) -> None:
#         self.item = User.objects.create(
#         email="123@gmail.com",
#         name="user",
#         password="pass",
#         )
#
#         self.user = User.objects\
#             .create_superuser(email="admin@gmail.com",
#                               name="admin",
#                               password="admin")
#
#         self.client.login(email='admin@gmail.com',
#                           password='admin')
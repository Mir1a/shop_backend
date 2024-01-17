# region				-----External Imports-----
from django.db import models
from django.utils import timezone
from django.contrib import auth
# endregion

# region				-----Internal Imports-----
from . import managers
# endregion

# region			  -----Supporting Variables-----
# endregion


class User(auth.models.AbstractBaseUser,
           auth.models.PermissionsMixin):
    # region              -----Information-----
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='users/avatar', null=True, blank=True)
    born = models.DateField(default=timezone.now, null=True, blank=True)
    # endregion

    # region       -----Private Information-----
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=255, null=False, blank=False)
    # endregion

    # region              -----Relation-----
    favorites = models.ManyToManyField(to="product.Item")
    # endregion

    # region              -----Metas-----
    class Meta:
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"

    REQUIRED_FIELDS = ["password"]
    USERNAME_FIELD = "email"
    # endregion

    # region         -----Default Methods-----
    def __str__(self):
        return str(self.id)
    # endregion

    # region             -----Manager-----
    objects = managers.CustomAccountManager()
    # endregion


def is_exists(id):
    User.objects.filter(id=id).exists()
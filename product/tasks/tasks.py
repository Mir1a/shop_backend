# region				-----External Imports-----
from random import randint

from ..models import Item
from celery.schedules import crontab
from django.conf import settings
from django.core import mail
from django.db import models
import celery
from django import utils
from django.utils import timezone
from django.db.models import ValueRange
# endregion

# region				-----Internal Imports-----
# endregion

# region			  -----Supporting Variables-----
# endregion


@celery.shared_task(name="cost_up")
def cost_up()\
        -> None:
    project_query = Item.objects.all()
    for item in project_query:
        item.price += 5
        item.save()

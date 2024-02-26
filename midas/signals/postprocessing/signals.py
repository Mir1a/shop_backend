from django.db.models.signals import post_save
from django.dispatch import receiver
from ...models import User as midas_user

@receiver(post_save, sender=midas_user)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print("hello")
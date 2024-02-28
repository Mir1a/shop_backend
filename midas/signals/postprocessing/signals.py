from django.db.models.signals import post_save
from django.dispatch import receiver
from ... import models
from django.conf import settings
import logging
import smtplib
#from ....secretshop import django
#from secretshop import mail_settings

# region                 -----Emails settings-----
password = "buvloplwstlzvlph"
email_sender = "miriamotuss@gmail.com"
smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.starttls()
smtp_server.login(email_sender, password)
# endregion

@receiver(post_save, sender=models.User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        email_getter = instance.email
        smtp_server.sendmail(email_sender, email_getter,  "hello")
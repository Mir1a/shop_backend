from django.contrib import admin

from .models import User
from .models import Transaction
from .models import Item
from .models import Order
from .models import Supply
# Register your models here.
admin.site.register(User)
admin.site.register(Transaction)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Supply)
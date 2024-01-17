from django.contrib import admin
from .models import Item
from .models import Order
from .models import Supply

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Supply)
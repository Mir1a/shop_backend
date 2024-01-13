from django.contrib import admin

from .models import user
from .models import transaction
from .models import item
from .models import order
from .models import supplies
# Register your models here.
admin.site.register(user)
admin.site.register(transaction)
admin.site.register(item)
admin.site.register(order)
admin.site.register(supplies)
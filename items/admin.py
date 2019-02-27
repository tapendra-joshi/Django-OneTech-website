from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.items_table)
admin.site.register(models.user_table)
admin.site.register(models.CategoryTable)
admin.site.register(models.CartTable)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)
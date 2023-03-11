from django.contrib import admin
from .models import ShoppingList, ShoppingItem, ItemsAdmin
# Register your models here.

admin.site.register(ShoppingList)
admin.site.register(ShoppingItem, ItemsAdmin)

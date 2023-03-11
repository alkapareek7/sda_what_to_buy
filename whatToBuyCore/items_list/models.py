from django.db.models import (
CASCADE, CharField, ForeignKey, Model, BooleanField, DateField)
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.admin import ModelAdmin

class ItemsAdmin(ModelAdmin):

    
    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description=None)

    ordering = ['id']
    list_display = ['id', 'name', 'shopping_list','description', 'is_completed']
    list_display_links = ['id', 'name']
    list_per_page = 3
    list_filter = ['description']
    search_fields = ['name']
    actions = ['cleanup_description']
    fieldsets = [
        (None, {'fields': ['name']}),
        (
        'Link another table',
        {
            'fields': ['shopping_list'],
            'description': (
                'Select from the list of possible lists'
                
            )
        }
        ),
        (
        'User Information',
        {
            'fields': ['description'],
            'description': 'These fields are intended to be filled in by our users.'
        }
        )
  ]
readonly_fields = ['is_completed']



class ShoppingList(Model):
    title = CharField('Shopping list name', max_length=100)
    user = ForeignKey(User, on_delete = CASCADE)
    created_at = DateField(default=datetime.now())
    is_public = BooleanField(default=False)
    no_sugar = BooleanField(default=False)


    def __str__(self):
        return self.title

class ShoppingItem(Model):
    name = CharField("Shopping list item name", max_length=100)
    description = CharField("Shopping list item description", max_length=300, null =True, blank = True)
    is_completed = BooleanField(default=False)
    shopping_list = ForeignKey(ShoppingList, on_delete=CASCADE)

    def __str__(self):
        return self.name

    def  get_absolute_url(self):
        return reverse('items-list', kwargs={"pk": self.shopping_list.pk})
    
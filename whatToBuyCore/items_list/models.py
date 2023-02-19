from django.db.models import (
CASCADE, CharField, ForeignKey, Model, BooleanField)
from django.urls import reverse
from django.contrib.auth.models import User

class ShoppingList(Model):
    title = CharField('Shopping list name', max_length=100)
    user = ForeignKey(User, on_delete = CASCADE)

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
    
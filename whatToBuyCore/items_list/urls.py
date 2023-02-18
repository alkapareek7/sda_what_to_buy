
from django.urls import path, include
from .views import my_lists, items_list, ItemCrateView, ItemDeleteView, ItemUpdateView

urlpatterns = [
    path("my_lists/", my_lists, name="lists-list"),
    path("my_lists/<pk>", items_list, name= "items-list"),
    path("item/add/", ItemCrateView.as_view(), name= 'item-add'),
    path("item/<int:pk>/update/", ItemUpdateView.as_view(), name="item-update"),
    path("item/<int:pk>/delete/", ItemDeleteView.as_view(), name="item-delete")
]
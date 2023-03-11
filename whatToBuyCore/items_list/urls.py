
from django.urls import path, include
from .views import my_lists, items_list , home, public_list, sugarfree
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", home, name="index"), 
    path("my_lists/", login_required(my_lists), name="lists-list"),
    path("my_lists/<pk>/", login_required(items_list), name= "items-list"),
    path("public_list/", public_list, name= "public-lists"),
    path("sugarfree/", sugarfree, name= "sugar-free")
    
]
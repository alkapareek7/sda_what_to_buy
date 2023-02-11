
from django.urls import path, include
from . import views

urlpatterns = [
    path("potato/<anything>", views.hello),
    path("potato/", views.hello2),
    
]
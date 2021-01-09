from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products/<int:id>', views.product)
]
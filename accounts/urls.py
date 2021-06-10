from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product, name='product'),
    path('customer/<int:pk>', views.customer, name='customer'),
    path('create_order/', views.createOrder, name='create_order'),
    path('update_order/<int:pk>', views.updateOrder, name='update_order'),
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Product
    path('products/', views.product, name='product'),
    
    # Customer
    path('customer/<int:pk>', views.customer, name='customer'),

    # Order
    path('create_order/<int:pk>', views.createOrder, name='create_order'),
    path('update_order/<int:pk>', views.updateOrder, name='update_order'),
    path('delete_order/<int:pk>', views.deleteOrder, name='delete_order'),
]

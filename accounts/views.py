from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    context = {
        "customers": customers,
        "orders": orders,
    }

    return render(request, "accounts/dashboard.html", context)


def product(request):
    all_products = Product.objects.all()
    return render(request, "accounts/products.html", {"all_prod": all_products})


def customer(request):
    return render(request, "accounts/customer.html")

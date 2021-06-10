from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

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


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'orders_count': orders_count}
    return render(request, "accounts/customer.html", context)

def createOrder(request):
    form = OrderForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, "accounts/order_form.html", context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request, "accounts/order_form.html", context)
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    total_customers = Customer.objects.all().count()
    orders = Order.objects.all()
    total_orders = Order.objects.all().count()
    orders_delivered = Order.objects.filter(status='Delivered').count()
    orders_pending = Order.objects.filter(status='Pending').count()
    context = {
        "customers": customers,
        "total_customers": total_customers,
        "orders": orders,
        "total_orders": total_orders,
        "orders_delivered": orders_delivered,
        "orders_pending": orders_pending,
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
            return redirect('home')
    
    return render(request, "accounts/order_form.html", context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    context = {
        'item': order
    }
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    
    return render(request, "accounts/delete.html", context)

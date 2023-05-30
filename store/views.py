from django.shortcuts import render
from product.models import Product
from order.models import Order
# Create your views here.


def home(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'home.html', context)


def single(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product':product
    }
    return render(request, 'single.html', context)


def shopping(request):
    products = Product.objects.all()
    context = {
        'products':products
    }

    return render(request, 'shopping.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context = {
        'items':items
    }
    return render(request, 'cart.html')
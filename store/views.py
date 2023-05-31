from django.shortcuts import render
from product.models import Product
from order.models import Order, OrderItem
from profil.models import Profil
from account.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse# Create your views here.
import json


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

@login_required(login_url='login')
def shopping(request):
    if request.user.is_authenticated:
        user = request.user
        id =user.id
        customer = Profil.objects.get(user=id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {
        'products':products, 'cartItems':cartItems
    }

    return render(request, 'shopping.html', context)

@login_required(login_url='login')
def cart(request, name):
    if request.user.is_authenticated:
        user = User.objects.get(username=name)
        id =user.id
        customer = Profil.objects.get(user=id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {
        'items':items,
        "order":order,
        'cartItems':cartItems,
    }
    return render(request, 'cart.html', context)


@login_required(login_url='login')
def checkout(request, name):
    if request.user.is_authenticated:
        user = User.objects.get(username=name)
        id =user.id
        customer = Profil.objects.get(user=id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0}

    context = {
        'items':items,
        "order":order,
    }
    return render(request, 'checkout.html', context)


def updateItem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action =='add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action =='remove':
        orderItem.quantity = (orderItem.quantity-1)

    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse('Item was deleted', safe=False)

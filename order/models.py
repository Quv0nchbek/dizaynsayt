from django.db import models
from product.models import Product
from profil.models import Profil
from uuid import uuid4

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Profil, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid4)

    def __str__(self):
        return f"Buyurtma --- ID: {self.transaction_id} --- {self.customer}"

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


    


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.order.transaction_id} -- | -- Buyurtma mahsuloti --- {self.product} -- | -- Miqdori: {self.quantity} -- | -- Vaqt: {self.date_added}"

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Profil, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.customer.manzil






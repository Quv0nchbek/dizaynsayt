from django.urls import path
from .views import home, shopping, single, cart, checkout, updateItem

urlpatterns = [
    path('', home, name='home'),
    path('xarid', shopping, name='shopping'),
    path('product/<int:pk>', single, name='single'),
    path('savatcha/<str:name>', cart, name='cart'),
    path('checkout/<str:name>', checkout, name='checkout'),
    path('update_item', updateItem, name='update_item'),
]
from django.urls import path
from .views import home, shopping, single, cart

urlpatterns = [
    path('', home, name='home'),
    path('xarid', shopping, name='shopping'),
    path('product/<int:pk>', single, name='single'),
    path('savatcha', cart, name='cart')
]
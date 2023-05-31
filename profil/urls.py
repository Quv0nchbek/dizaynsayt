from django.urls import path
from .views import profil_user

urlpatterns =[
    path('<str:name>', profil_user, name='profil')
]
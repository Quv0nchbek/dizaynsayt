from django.shortcuts import render
from .models import Profil
from account.models import User
# Create your views here.

def profil_user(request, name):
    user = User.objects.get(username=name)
    profil_user = Profil.objects.get(user=user.id)

    context = {
        'profil_user':profil_user
    }
    return render(request, 'accounts/profil.html', context)
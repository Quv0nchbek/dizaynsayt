from django.shortcuts import render

# Create your views here.


def login_user(request):
    return render(request, 'accounts/login.html')

def signup_user(request):
    return render(request, 'accounts/registration.html')
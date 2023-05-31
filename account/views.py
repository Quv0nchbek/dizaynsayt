from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm


# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Error')


    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    print('Log out')
    return redirect('/')

def signup_user(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            return redirect('login')

    context = {
        "form": form,
    }
    return render(request, 'accounts/register.html', context)
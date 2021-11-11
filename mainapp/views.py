from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):

    return render(request, 'mainapp/index.html',{
        'title': 'Home'
    })

def about(request):

    return render(request, 'mainapp/about.html',{
        'title': 'About us'
    })

def register_page(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Welcome to lavastage')

                return redirect('home')

        return render(request, 'users/register.html',{
            'title': 'Register',
            'register_form': register_form
        })

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            
            else:
                messages.warning(request,'Failed login')

        return render(request, 'users/login.html',{
            'title': 'Login',

        })

def logout_user(request):
    logout(request)
    return redirect('login')
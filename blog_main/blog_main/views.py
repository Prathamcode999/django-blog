from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from .forms import registrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib import messages

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    posts = Blog.objects.filter(is_featured = False ,status='Published')
    context = {
        'category': categories, 
        'Featured_posts': featured_posts,
        'post': posts
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        Form = registrationForm(request.POST)
        if Form.is_valid():
            Form.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')
    else:
        Form = registrationForm()
    context = {
        'form': Form
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        Form = AuthenticationForm(request,request.POST)
        if Form.is_valid():
            username = Form.cleaned_data.get('username')
            password = Form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password) 
            if user is not None:
                auth.login(request, user)
                return redirect('home')          
    Form = AuthenticationForm()
    context = {
        'form': Form
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')
    

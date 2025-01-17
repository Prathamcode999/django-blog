from django.shortcuts import render
from blogs.models import Category, Blog

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
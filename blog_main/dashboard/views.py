from django.shortcuts import get_object_or_404, redirect, render
from .form import CategoryForm
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    categories = Category.objects.all().count()
    blogs = Blog.objects.all().count()
    context = {
        'category_count' : categories,
        'blog_count' : blogs,
    }
    return render(request, 'dashboard/dashboard.html',context)

def categories(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
    }
    return render(request, 'dashboard/categories.html',context)


def add_category(request):
    if request.method == 'POST':# 
        form = CategoryForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    context = {
        'Form' : form,
    }
    return render(request, 'dashboard/add_category.html',context)

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
        
    form = CategoryForm(instance=category)
    context = {
        'Form' : form,
        'Category' : category,
    }
    return render(request, 'dashboard/edit_category.html',context)

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

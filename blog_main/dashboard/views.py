from django.shortcuts import get_object_or_404, redirect, render
from .form import CategoryForm, PostForm, UserForm, EditUserForm
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

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
    if request.method == 'POST':
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


def posts(request):
    posts = Blog.objects.all()
    context = {
        'Posts' : posts,
    }
    return render(request, 'dashboard/posts.html',context)

@permission_required('app.add_post', raise_exception=True)
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False) # creates an object and the form is saved inside the object
            post.author = request.user # the object can is now accessible
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts') 
    form = PostForm()
    context={
        'Form' : form,
    }
    return render(request,'dashboard/add_post.html',context)

def edit_post(request, pk):
    blog = Blog.objects.get(pk=pk)  # Fetch the blog post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('posts')
    form = PostForm(instance=blog)
    context = {
        'Form': form,
        'blog': blog,
    }
    return render(request, 'dashboard/edit_post.html', context)


def delete_post(request, pk):
    blog = get_object_or_404(Blog,pk=pk)
    blog.delete()
    return redirect('posts')


def user(request):
    user = User.objects.all()
    context = {
        'user':user,
    }
    return render(request, 'dashboard/user.html',context)

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user') 
    form = UserForm()
    context={
        'Form' : form,
    }
    return render(request, 'dashboard/add_user.html', context)

def edit_user(request, pk):
    user = User.objects.get(pk=pk)  
    if request.method == 'POST':
        form = EditUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('user')
    form = EditUserForm(instance=user)
    context = {
        'Form': form,
        'user': user,
    }
    return render(request, 'dashboard/edit_user.html', context)
    
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('user')
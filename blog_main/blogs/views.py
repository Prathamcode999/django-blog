from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import Blog, Category
from django.db.models import Q

# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status = 'Published' ,category=category_id)
    try:
        category = Category.objects.get(id=category_id)
    except:
        return redirect('home')

    context = {
        'post': posts,
        'Category': category,
    }
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    single_post = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'post': single_post,
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    Blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context = {
        'blogs': Blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)
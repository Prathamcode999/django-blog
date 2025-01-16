from .models import Category

def categories_name(request):
    categories = Category.objects.all()
    return dict(category=categories)
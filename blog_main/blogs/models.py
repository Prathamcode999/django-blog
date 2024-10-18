from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField( max_length=50, unique=True)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories" #by default djnago names it as categorys so to change the name we use meta

    def __str__(self):
        return self.category_name


STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published","Published")
)


class Blog(models.Model):
    title= models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE) # it creates a relationship with Category model with their inbuit primary key
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField( upload_to='uploads/%y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body=models.TextField(max_length=2000)
    status= models.CharField(choices=STATUS_CHOICES, max_length=20, default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
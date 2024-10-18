from django.contrib import admin
from . models import Category, Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)} #this allows the slug to autogenerate wrt to title field ( , is imp)
    list_display = ('title','category','author', 'status','is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status') # category is foregin key with the help which we go to category model and then call the category_name
    list_editable = ('is_featured',) #allows you to edit the option directly thorugh admin main panel instead on going inside to mark uncheck and then save

admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
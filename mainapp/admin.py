from django.contrib import admin
from mainapp.models import Blog, Service, Product, Category,BlogCategory,Images
# Register your models here.
admin.site.register(Service)
admin.site.register(Blog)
admin.site.register(BlogCategory)

admin.site.register(Category)

class BookInline(admin.TabularInline):  
    model = Images
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Product, AuthorAdmin)

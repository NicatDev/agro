from django.contrib import admin
from mainapp.models import Instagram,Partner,Blog, Service, Product, Category,BlogCategory,Images,Message
# Register your models here.
admin.site.register(Service)
admin.site.register(Blog)
admin.site.register(BlogCategory)
admin.site.register(Partner)
admin.site.register(Category)

class BookInline(admin.TabularInline):  
    model = Images
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Product, AuthorAdmin)
admin.site.register(Instagram)
admin.site.register(Message)
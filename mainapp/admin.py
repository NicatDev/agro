from django.contrib import admin
from mainapp.models import Instagram,Partner,Blog, Service, Product, Category,BlogCategory,Images,Message
from modeltranslation.admin import TranslationAdmin

class TranslateAdmin(TranslationAdmin):

    class Media:

        group_fieldsets = True 

        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        } 

admin.site.register(Service)
admin.site.register(Blog,TranslateAdmin)
admin.site.register(BlogCategory,TranslateAdmin)
admin.site.register(Partner)
admin.site.register(Category,TranslateAdmin)

class ProductInline(admin.TabularInline):  
    model = Images
    extra = 0

class ProductAdmin(TranslationAdmin):
    inlines = [ProductInline]

    class Media:

        group_fieldsets = True 

        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Product, ProductAdmin)
admin.site.register(Instagram)
admin.site.register(Message)
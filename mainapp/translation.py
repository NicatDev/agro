from modeltranslation.translator import TranslationOptions,register, translator
from mainapp.models import *


class NameTranslationOption(TranslationOptions):
    fields = ('name',)


class ProductTranslationOption(TranslationOptions):
    fields = ('name','description','location',)
  
class BlogTranslationOption(TranslationOptions):
    fields = ('title','content','content_bottom')

translator.register(Category, NameTranslationOption)
translator.register(Product, ProductTranslationOption)
translator.register(Blog, BlogTranslationOption)
translator.register(BlogCategory,NameTranslationOption)


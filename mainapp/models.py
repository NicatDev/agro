from django.db import models
from django.contrib.auth import get_user, get_user_model
from mainapp.utils import *
from datetime import datetime
from django.utils.text import slugify
from django.urls import reverse


class BaseMixin(models.Model):
    slug = models.SlugField(unique=True,editable=False,blank=True,null=True)
    created_at = models.DateField(auto_now=True,blank=True,null=True,)
    
    class Meta:
        abstract = True

class MetaMixin(models.Model):
    seo_title = models.CharField(max_length=1200,null=True,blank=True,verbose_name='title for seo')
    seo_keyword = models.CharField(max_length=1200,null=True,blank=True,verbose_name='keyword for seo')
    seo_alt = models.CharField(max_length=1200,null=True,blank=True)
    seo_description = models.CharField(max_length=1200,null=True,blank=True,verbose_name='description for seo')
        
    class Meta:
        abstract = True

class Blog(BaseMixin,MetaMixin):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    
class Product(BaseMixin,MetaMixin):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    stock_weight = models.PositiveBigIntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name    

class Images(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Service(BaseMixin,MetaMixin):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
    
class Message(models.Model):
    full_name = models.CharField(max_length = 200)
    email = models.EmailField()
    subject = models.CharField(max_length = 200)
    message = models.TextField()

    def __str__(self):
        return self.full_name    





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
    
class Product(MetaMixin,BaseMixin):
    name = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.SmallIntegerField(default=0)
    description = models.TextField()
    stock = models.BooleanField(default=True)
    category = models.ManyToManyField(Category)
    new = models.BooleanField(default=False)
    best_seller = models.BooleanField(default=False)
    most_searched = models.BooleanField(default=False)
    product_code = models.CharField(max_length = 300,null=True,blank=True)

    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = get_slug(self.name)
            if Product.objects.filter(slug=new_slug).exists():
                count = 0
                while Product.objects.filter(slug=new_slug).exists():
                    new_slug = f"{get_slug(self.name)}-{count}"
                    count += 1
            self.slug = new_slug
        super(Product, self).save(*args, **kwargs)
    
    def get_main_image(self):
        main_image = self.images.first()
        return main_image.image if main_image else None
    
    def get_discount_price(self):
        if self.discount_percent>0:
            discounted = self.price * (100-self.discount_percent) /100
        else:
            discounted = self.price
        return discounted

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





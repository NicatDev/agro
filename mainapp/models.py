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

class BlogCategory(BaseMixin):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return f'- {self.name}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = get_slug(self.name)
            if BlogCategory.objects.filter(slug=new_slug).exists():
                count = 0
                while BlogCategory.objects.filter(slug=new_slug).exists():
                    new_slug = f"{get_slug(self.name)}-{count}"
                    count += 1
            self.slug = new_slug
        super(BlogCategory, self).save(*args, **kwargs)
    
class Blog(BaseMixin,MetaMixin):
    category = models.ForeignKey(BlogCategory,on_delete = models.CASCADE,related_name='blogs')
    title = models.CharField(max_length=200)
    content = models.TextField()
    content_bottom = models.ImageField(null=True,blank=True)
    image = models.ImageField()

    def __str__(self):
        return f'- {self.title}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = get_slug(self.title)
            if Blog.objects.filter(slug=new_slug).exists():
                count = 0
                while Blog.objects.filter(slug=new_slug).exists():
                    new_slug = f"{get_slug(self.title)}-{count}"
                    count += 1
            self.slug = new_slug
        super(Blog, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blogSingle', kwargs={'slug': self.slug})
    
class Category(BaseMixin):
    name = models.CharField(max_length = 200)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return f'- {self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = get_slug(self.name)
            if Category.objects.filter(slug=new_slug).exists():
                count = 0
                while Category.objects.filter(slug=new_slug).exists():
                    new_slug = f"{get_slug(self.name)}-{count}"
                    count += 1
            self.slug = new_slug
        super(Category, self).save(*args, **kwargs)

class Product(MetaMixin,BaseMixin):
    name = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.SmallIntegerField(default=0)
    description = models.TextField(null=True,blank=True)
    stock = models.BooleanField(default=True)
    stock_value = models.IntegerField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name="products")
    new = models.BooleanField(default=False)
    best_seller = models.BooleanField(default=False)
    most_searched = models.BooleanField(default=False)
    product_code = models.CharField(max_length = 300,null=True,blank=True)
    location = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return f'- {self.name}'

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
    
    def get_secondary_image(self):
        if self.images.count() > 1:
            image = self.images[1]
        else:
            image = self.images.first()
        return image.image if image else None

    def get_discount_price(self):
        if self.discount_percent>0:
            discounted = self.price * (100-self.discount_percent) /100
        else:
            discounted = self.price
        return discounted

    def get_absolute_url(self):
        return reverse('shopSingle', kwargs={'slug': self.slug})
    
class Images(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')

    def __str__(self):
        return f'- {self.product.name}'

class Service(BaseMixin,MetaMixin):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return f'- {self.name}'
    
class Message(models.Model):
    name = models.CharField(max_length = 200)
    surname = models.CharField(max_length = 200)
    email = models.EmailField()
    phone = models.CharField(max_length = 200)
    message = models.TextField()

    def __str__(self):
        return f'- {self.name} - {self.surname}'    


class Partner(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'- {self.name}'

class Instagram(models.Model):
    image = models.ImageField()
    href = models.CharField(max_length = 200)

    def __str__(self):
        return self.pk

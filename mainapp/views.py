from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from mainapp.models import *
from django.urls import translate_url
from django.db.models import Q,F,FloatField,Count
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Count
from django.conf import settings
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def home(request):

    services = Service.objects.all()[:3]
    products = Product.objects.all().order_by('-created_at')[:4]
    blogs = Blog.objects.all()[:2]
    categories = Category.objects.all()

    context = {
        'categories':categories,
        'services':services,
        'products':products,
        'blogs':blogs
    }

    return render(request,'index-2.html',context)

def about(request):
    
    services = Service.objects.all()[:3]
    products = Product.objects.all().order_by('-created_at')[:4]
    blogs = Blog.objects.all()[:2]
    categories = Category.objects.all()
    duration_increment = 300
    for index, obj in enumerate(categories):
        obj.duration = duration_increment * (index + 1)
    partners = Partner.objects.all()
    instagram = Instagram.objects.all()
    context = {
        'partners':partners,
        'categories':categories,
        'services':services,
        'products':products,
        'blogs':blogs
    }

    return render(request,'about-us.html',context)

def shop(request):
    categories = Category.objects.all()

    product_query = Product.objects.all()
    if request.GET.get('categories'):
        product_query = product_query.filter(category__slug=request.GET.get('categories'))
    if request.GET.get('ordering'):
        if request.GET.get('ordering') == 'price':
            product_query = product_query.order_by('price')
    if request.GET.get('search'):
        product_query = product_query.filter(
        Q(name__icontains=request.GET.get('search')) | Q(description__icontains=request.GET.get('search'))
    )
    paginator = Paginator(product_query, 4)
    page = request.GET.get("page", 1)
    products = paginator.get_page(page)
    total_pages = [x+1 for x in range(paginator.num_pages)]

    trending_products = Product.objects.all()[:]
    context = {
        'products':products,
        'total_pages':total_pages,
        'categories':categories
    }

    return render(request,'shop-list-sidebar.html',context)

def shopSingle(request,slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.exclude(slug=slug)[0:4]
    context = {
        'product':product,
        'related_products':related_products
    }
    return render(request,'product-detail.html',context)

def blogs(request):
    blog_list = Blog.objects.all()

    if request.GET.get('category'):
        blog_list = blog_list.filter(category__slug=request.GET.get('category'))
        print(blog_list,'++++')
    paginator = Paginator(blog_list, 4)
    page = request.GET.get("page", 1)
    blogs = paginator.get_page(page)
    total_pages = [x+1 for x in range(paginator.num_pages)]
    categories = BlogCategory.objects.all()

    recent_blogs = Blog.objects.all()[::-1][:3]

    context = {
        'categories':categories,
        'blogs':blogs,
        'total_pages':total_pages,
        'recent_blogs':recent_blogs
    }
    return render(request,'blogs.html',context)

def blogSingle(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    related_blogs = Blog.objects.exclude(slug=slug)[0:4]
    context = {
        'blog':blog,
        'related_blogs':related_blogs
    }
    return render(request,'blog-details.html',context)

def contact(request):

    context = {

    }
    return render(request,'contact-us.html',context)

from .forms import Messageform
import json
def message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = Messageform(data=data)
        if message.is_valid():
            message.save()
        else:
            print(message.errors)
            return JsonResponse({'status':'error'}, status=400)
    return JsonResponse({'status': 'success'}, status=200)
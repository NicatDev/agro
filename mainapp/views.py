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


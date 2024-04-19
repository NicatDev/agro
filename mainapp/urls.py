from django.urls import path,include
from .views import *

urlpatterns = [
        path('',home,name='home'),
        path('mehsullar',shop,name='shop'),
        path('haqqimizda',about,name='about'),
        path('bloqlar',blogs,name='blogs'),
        path('elaqe',contact,name='contact'),
        path('message',message,name='message'),
        path('mehsul/<slug>',shopSingle,name='shopSingle'),
        path('bloq/<slug>',blogSingle,name='blogSingle'),
        
]

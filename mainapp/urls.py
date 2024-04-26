from django.urls import path,include
from .views import *

urlpatterns = [
        path('set-language/<lang_code>/<path:url>', set_language, name='set_language'),
        path('',home,name='home'),
        path('mehsullar',shop,name='shop'),
        path('haqqimizda',about,name='about'),
        path('xidmetler',services,name='services'),
        path('bloqlar',blogs,name='blogs'),
        path('elaqe',contact,name='contact'),
        path('message',message,name='message'),
        path('mehsul/<slug>',shopSingle,name='shopSingle'),
        path('bloq/<slug>',blogSingle,name='blogSingle'),
        
]

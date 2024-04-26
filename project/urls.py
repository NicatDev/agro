from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
# from marketapp.sitemap import BlogSiteMap,ServiceSitemap, StaticSitemap
from django.views.generic import TemplateView
from mainapp.sitemap import *

sitemaps = {
    'blog_sitemap': BlogSiteMap,
    'product_sitemap': ProductSiteMap,
    'static_sitemap': StaticSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt', content_type="text/plain")),
]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include("mainapp.urls")),
    re_path(r'^rosetta/', include('rosetta.urls')),
    path(
        'sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'
    ),
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt', content_type="text/plain")),
 
)

urlpatterns += static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


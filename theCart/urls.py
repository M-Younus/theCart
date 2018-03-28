"""theCart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

from shop import views

urlpatterns = [
    # url(r'^$', views.index,name='index'),
    # url(r'^cart/', include('cart.urls', namespace='cart')),
    # url(r'^(?P<CName>[-\w]+)/(?P<Pid>\d+)/$', views.product_detail, name='product_detail'),
    # url(r'^(?P<cat_id>\d+)/$', views.cat_related_products, name="cat_related_products"),
    # url(r'^admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('cart/', include('cart.urls')),
    # # path('CName/Pid/', views.product_detail, name='product_detail'),
    # path('cat_id/', views.cat_related_products,name="cat_related_products"),
    # path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


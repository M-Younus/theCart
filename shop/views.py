from django.shortcuts import render
from django.http import Http404

from shop.models import Category,Product

def index(request):
    categories=list(Category.objects.all())
    products=list(Product.objects.all())

    return render(request,'shop/index.html',{
        'categories':categories,
        'products':products
    });


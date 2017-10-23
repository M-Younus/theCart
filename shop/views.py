from django.shortcuts import render
from django.http import Http404

from shop.models import Category, Product


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'shop/index.html', {
        'categories': categories,
        'products': products
    })

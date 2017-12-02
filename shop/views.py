from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from shop.models import Category, Product


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'shop/index.html', {
        'categories': categories,
        'products': products
    })


def cat_related_products(request,cat_id):
    all_related_products=Product.objects.filter(category_id=cat_id).order_by('?')

    paginator=Paginator(all_related_products,25)

    page=request.GET.get('page')
    try:
        all_prods=paginator.page(page)
    except PageNotAnInteger:
        all_prods=paginator.page(1)
    except EmptyPage:
        all_prods=paginator.page(paginator.num_pages)

    context={
        'all_prods': all_prods,
    }

    return render(request,'shop/cat_related_prods_page.html',context)



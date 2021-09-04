from django.shortcuts import render, get_object_or_404
from .models import *
from category.models import *


def store(request,category_slug=None):

    category_req= None
    products = None

    if category_slug != None:

        category_req = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=category_req,is_available=True)
        products_count = products.count()
    else:
        products = Product.objects.filter(is_available=True)
        products_count = products.count()

    context = {
      'products': products,
      'products_count': products_count,
    }
    return render(request, 'store/store.html',context)


def product_detail(request, category_slug, product_slug):

    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context={
      'single_product':single_product,
    }
    return render(request,'store/product_detail.html',context)
# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.core.paginator import Paginator

def select(request):

    return render(request, 'select.html')

# def regionFilter(request, region):
#     regionPost = Products.objects.filter(region=region)
#     store = regionPost.first()
#     return render(request, 'select.html', {"regionPost":regionPost, "store":store})

def storeFilter(request, storeName):
    storePost = Products.objects.filter(storeName=storeName)
    return render(request, 'detail_store.html', {"storePost":storePost, "storeName": storeName})

def detail_product(request, product_id):
    store = get_object_or_404(Products, pk=product_id)
    return render(request, 'detail_product.html', {'store':store})

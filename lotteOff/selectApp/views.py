from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from django.core.paginator import Paginator

def select(request):
    all_product = Products.objects.all()


    return render(request, 'select.html', {'all_product': all_product})

def detail_product(request, product_id):
    store = get_object_or_404(Products, pk=product_id)
    return render(request, 'detail_product.html', {'store':store})

def storeFilter(request, storeName):
    storePost = Products.objects.filter(storeName=storeName)
    return render(request, 'detail_store.html', {"storePost":storePost, "storeName": storeName})

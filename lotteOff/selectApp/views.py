from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from django.core.paginator import Paginator

def select(request):
    return render(request, 'select.html')

def detail(request, store_id):
    store = get_object_or_404(Products, pk=store_id)
    return render(request, 'detail_store.html', {'store':store})


from django.shortcuts import render
from .models import NewProduct

def newProduct(request):
    all_new = NewProduct.objects.all()
    return render(request, "newProduct.html", {'news':all_new})
from django.shortcuts import render, get_object_or_404
from .models import NewProduct

def newProduct(request):
    all_new = NewProduct.objects.all()
    return render(request, "newProduct.html", {'news':all_new})

def newDetail(request, new_id):
    post = get_object_or_404(NewProduct, pk=new_id)
    return render(request, 'newDetail.html', {'post':post})
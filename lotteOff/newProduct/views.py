from django.shortcuts import render, get_object_or_404, redirect
from .models import NewProduct
from .forms import ApplyForm

def newProduct(request):
    all_new = NewProduct.objects.all()
    return render(request, "newProduct.html", {'news':all_new})

def newDetail(request, new_id):
    post = get_object_or_404(NewProduct, pk=new_id)
    apply_form = ApplyForm()
    return render(request, 'newDetail.html', {'post':post, 'apply_form':apply_form,})

def createApply(request, new_id):
    apply_form = ApplyForm(request.POST)
    if apply_form.is_valid():
        apply = apply_form.save(commit = False)
        apply.author = request.user
        apply.newProduct = NewProduct.objects.get(pk = new_id)
        apply.save()
        return redirect('newDetail', new_id)

def deleteApply(request, new_id, apply_id):
    apply = Apply.object.get(pk = apply_id)
    if request.user == apply.author:
        apply.delete()
        return redirect('newDetail', new_id)
    else:
        raise PermissionDenied
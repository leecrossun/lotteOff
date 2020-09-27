from django.shortcuts import render
from django.core.paginator import Paginator
from .models import DriveThru
# Create your views here.
def home(request):
    return render(request, 'home.html')

def driveThru(request):
    form = DriveThru.objects
    forms = DriveThru.objects.all()
    paginator = Paginator(forms,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'driveThru.html', {'form':form, 'posts':posts})

def new(request):
    return render(request, 'new.html')
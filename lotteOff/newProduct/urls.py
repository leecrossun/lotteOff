from django.urls import path
from . import views

urlpatterns = [
    path('newProduct/', views.newProduct, name='newProduct'),
    path('newProduct/<int:new_id>/', views.newDetail, name='newDetail'),
]
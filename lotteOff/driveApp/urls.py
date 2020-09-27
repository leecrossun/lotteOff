from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('driveThru/', views.driveThru, name='driveThru'),
    path('new/', views.new, name='new'),
]
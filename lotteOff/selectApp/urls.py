from django.urls import path
from . import views

urlpatterns = [
    path('select/', views.select, name="select"),
    path('detail/<int:store_id>', views.detail, name="detail"),
]
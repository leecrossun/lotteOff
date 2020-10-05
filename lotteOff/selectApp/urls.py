from django.urls import path, include   ### include 추가
from . import views

urlpatterns = [
    path('select/', views.select, name="select"),
    path('select/<str:region>', views.regionFilter, name="regionFilter"),
    path('detail_store/<str:storeName>', views.storeFilter, name="storeFilter"),
    path('detail_product/<int:product_id>', views.detail_product, name="detail_product"),
    path('', include('cartApp.urls', namespace='cart')),   ### url 추가
]
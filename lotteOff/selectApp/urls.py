from django.urls import path
from . import views

urlpatterns = [
    path('select/', views.select, name="select"),
    path('detail_product/<int:product_id>', views.detail_product, name="detail_product"),
    path('detail_store/<str:storeName>', views.storeFilter, name="storeFilter"),
]
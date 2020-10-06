from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('driveApp.urls')),
    path('', include('selectApp.urls')),
    path('', include('newProduct.urls')),
    path('', include('chatApp.urls')),
    path('', include('cartApp.urls', namespace="cart")),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


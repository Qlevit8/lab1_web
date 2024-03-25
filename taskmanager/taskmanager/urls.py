from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pet_shop.api.urls')),
    path('pet-shop/', include('pet_shop.urls')),
]

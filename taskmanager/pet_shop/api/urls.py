from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.get_users),
    path('api/pets/', views.get_pets),
    path('api/add_pet/', views.add_pet),
    path('api/search_pet/', views.search_pets_by_name),
    path('api/search_user/', views.search_user_by_id)
]
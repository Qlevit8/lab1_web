from django.urls import path

from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/notification/', WSConsumer.as_asgi())
]

from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from taskmanager.celery import app
from .service import send_email, inflation
from .models import User, Species
from django.core.mail import send_mail
from .views import set_swines
from django.db.models import F


@app.task
def send_beat_email():
    users = User.objects.filter(name='Михайло')
    for user in users:
        send_mail(
            'Повідомлення кожні 5 хвилин',
            'Це повідомлення шлеться кожні 5 хвилин усім користувачам.',
            'django.celery.test8@gmail.com',
            [user.email],
            fail_silently=False
        )
    send_message('Пошта відправлена всім користувачам з іменем "Михайло"')


@app.task
def increase_prices():
    Species.objects.update(species_price=F('species_price') + 1)
    send_message('Ціни підвищено на 1')


def send_message(message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'notification',
        {
            'type': 'task_message',
            'message': message,
        }
    )

from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Species
from django.db.models import F
from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json
from celery import shared_task
import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_email(user_email, message, article):
    send_mail(
        article,
        message,
        'django.celery.test8@gmail.com',
        [user_email],
        fail_silently=False
    )


def inflation(num):
    Species.objects.update(species_price=F('species_price') + num)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'notification',
        {
            'type': 'task_message',
            'message': 'hello world',
        }
    )


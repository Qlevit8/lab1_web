import os
from celery import Celery
from celery.schedules import crontab
from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')

app = Celery('taskmanager')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.task_queues = (
    Queue('default', Exchange('default'), routing_key='task.#'),
    Queue('email', Exchange('email'), routing_key='email.#'),
    Queue('long_running', Exchange('long_running'), routing_key='long_running.#'),
)

app.conf.task_routes = {
    'pet_shop.tasks.send_beat_email': {'queue': 'email', 'routing_key': 'email.task'},
    'pet_shop.tasks.increase_prices': {'queue': 'long_running', 'routing_key': 'long_running.task'},
}

app.conf.beat_schedule = {
    'inflation-every-1-min': {
        'task': 'pet_shop.tasks.increase_prices',
        'schedule': crontab(minute='*/1'),
        'options': {'queue': 'long_running'},
    },
    'send-mail-every-5-min': {
        'task': 'pet_shop.tasks.send_beat_email',
        'schedule': crontab(minute='*/5'),
        'options': {'queue': 'email'},
    }
}
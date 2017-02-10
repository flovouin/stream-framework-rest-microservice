import os
from celery import Celery

app = Celery('activity')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "activity.settings")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(['stream_framework'])

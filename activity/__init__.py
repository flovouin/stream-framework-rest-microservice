import os
from celery import Celery

# This is used when the service is run by Celery, as a worker.
app = Celery('activity')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "activity.settings")
app.config_from_object('django.conf:settings', namespace='CELERY')
# Relevant tasks are stored in Stream-Framework, but we still need the service code because the
# feed manager is also needed and serialised by Celery.
app.autodiscover_tasks(['stream_framework'])

#!/usr/bin/env python

from celery import current_app
current_app.conf.CELERY_ALWAYS_EAGER = True
current_app.conf.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
current_app.conf.broker_url = 'pyamqp://rabbitmq'

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "activity.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

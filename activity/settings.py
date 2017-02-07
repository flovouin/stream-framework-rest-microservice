import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'us%!@&39o250e79)l!4*0ac4oquo+^nm83vp#y%mw9i$7)i&fy'

DEBUG = True
ALLOWED_HOSTS = ['*']

# Stream-framework related

STREAM_CASSANDRA_HOSTS = ['cassandra']
CASSANDRA_DRIVER_KWARGS = {
    'protocol_version': 3
}

# Application definition

INSTALLED_APPS = [
    'activity',
    'django.contrib.contenttypes',
    'rest_framework'
]

REST_FRAMEWORK = {
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'PAGE_SIZE': 10
}

MIDDLEWARE = ['django.middleware.common.CommonMiddleware']

ROOT_URLCONF = 'activity.urls'

WSGI_APPLICATION = 'activity.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

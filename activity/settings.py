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
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework'
]

REST_FRAMEWORK = {
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'activity.authentication.NarralyJSONWebTokenAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    'DEFAULT_PARSER_CLASSES': ['rest_framework.parsers.JSONParser'],
    'PAGE_SIZE': 10
}

JWT_AUTH = {
    'JWT_PUBLIC_KEY': '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3bU3bOIJpaD8SjNEzZ5a
BGJlm+kgPdvgVtl2oU/gUsZUa3Kwpvv/OMuM1XpFNGIlkSfQCsHdvLZy0KCjXb0m
nGfWuqKw84u0XswnT20OBHu88VL/RmHFCrnhuUr0nhG2QL106uH/iQDRxqbfxBXa
wiL95fMJlAvUHdavzIhb+YtMIWbPF95RPb3AmyDEWAPag7Ar4sBXg/j41dSdFvLS
r7tjM67K1IkDDhpQd3DdTLQPJCvdY/1xkDqbhO0XHiXvD6R8OyTHGq8oU4gpzcjA
FX35Pxi66D2BmB3rWJRqjozLjyb3DC0VyPExIKfo5H9VstDWY8ZfESYuaJK1XVLe
lQIDAQAB
-----END PUBLIC KEY-----
''',
    'JWT_ALGORITHM': 'RS256'
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    # 'JWT_AUDIENCE': None,
    # 'JWT_ISSUER': None,
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

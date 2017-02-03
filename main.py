from celery import current_app

current_app.conf.CELERY_ALWAYS_EAGER = True
current_app.conf.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
current_app.conf.broker_url = 'pyamqp://rabbitmq'

from stream_framework import settings

settings.STREAM_CASSANDRA_HOSTS = ['cassandra']
settings.CASSANDRA_DRIVER_KWARGS = {
    'protocol_version': 3
}

from activity import server

if __name__ == "__main__":
    server.app.run(host='0.0.0.0')

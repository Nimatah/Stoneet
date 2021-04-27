import os
from .base import *

USE_X_FORWARDED_HOST = True

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'planhub',
        'USER': 'planhub',
        'PASSWORD': os.getenv('DJANGO_DATABASE_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
    },
}

HUEY = {
    'huey_class': 'huey.RedisHuey',
    'name': "plantask",
    'results': True,
    'store_none': False,
    'immediate': False,
    'utc': False,
    'blocking': True,
    'connection': {
        'host': 'redis',
        'port': 6379,
        'db': 1,
        'connection_pool': None,
        'read_timeout': 1,
    },
    'consumer': {
        'workers': 1,
        'worker_type': 'thread',
        'initial_delay': 0.1,
        'backoff': 1.15,
        'max_delay': 10.0,
        'scheduler_interval': 1,
        'periodic': True,
        'check_worker_health': True,
        'health_check_interval': 1,
    },
}

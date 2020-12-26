import os

from .base import *

USE_X_FORWARDED_HOST = True

DEBUG = True

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

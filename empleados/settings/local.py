from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  'dbempleado',
        'USER':  'diego',
        'PASSWORD':  'costume',
        'HOST':  'localhost',
        'PORT':  '5432',
    }
}

STATIC_URL = 'static/'
from .base import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd30il9ibgijs4l',
        'USER': 'irxukxprszsmwj',
        'PASSWORD': 'bfb2fde7829666175e47e3c387287b6d58329375391dbf7be8cc599a3e01c572',
        'HOST': 'ec2-34-198-186-145.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

django_heroku.settings(locals())



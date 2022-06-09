from .base import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

django_heroku.settings(locals())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd30il9ibgijs4l',
        'USER': 'irxukxprszsmwj',
        'PASSWORD': 'bfb2fde7829666175e47e3c387287b6d58329375391dbf7be8cc599a3e01c572',
        'HOST': 'ec2-34-198-186-145.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
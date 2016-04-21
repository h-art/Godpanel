from base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret key'

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbaname',
        'USER': 'dbuser',
        'PASSWORD': 'dbpass',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

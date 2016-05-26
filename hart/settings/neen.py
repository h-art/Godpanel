import os
from hart.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['PG_DB'],
        'USER': os.environ['PG_USER'],
        'PASSWORD': os.environ['PG_PASS'],
        'HOST': os.environ['PG_HOST'],
        'PORT': '5432',
    }
}

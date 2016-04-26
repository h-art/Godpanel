from hart.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '699-1jeezr%^!qmn3!s33t@&=p4@v+5!2hql6q%^99@ph*n+(3'

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hart',
        'USER': 'mrosati',
        'PASSWORD': 'Qu3enai5',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

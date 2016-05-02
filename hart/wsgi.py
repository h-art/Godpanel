"""
WSGI config for godpanel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import configparser

from django.core.wsgi import get_wsgi_application

parser = configparser.ConfigParser()

try:
    filename = os.path.realpath(os.path.join(os.path.dirname(__file__), '.config.ini'))
    parser.read_file(open(filename))
    django_settings_module = parser.get('wsgi', 'django_settings_module')
except FileNotFoundError:
    django_settings_module = 'hart.settings.local'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_module)

application = get_wsgi_application()

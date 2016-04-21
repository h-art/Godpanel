"""
WSGI config for godpanel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

env = os.getenv('DJANGO_ENV')

if env is None:
  env = 'local'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", '.'.join(["godpanel.settings", env]))

application = get_wsgi_application()

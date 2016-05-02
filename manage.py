#!/usr/bin/env python
import os
import sys
import configparser

if __name__ == "__main__":
    parser = configparser.ConfigParser()

    try:
        filename = os.path.realpath(os.path.join(os.path.dirname(__file__), '.config.ini'))
        parser.read_file(open(filename))
        django_settings_module = parser.get('wsgi', 'django_settings_module')
    except FileNotFoundError:
        django_settings_module = 'hart.settings.local'

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_module)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

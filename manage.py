#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    env = os.getenv('DJANGO_ENV')

    if env is None:
        env = 'local'

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", '.'.join(["hart.settings", env]))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

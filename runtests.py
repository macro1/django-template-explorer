import os
import sys
import django
from django.core import management


def runtests():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "tests.settings")
    try:
        django.setup()
    except AttributeError:
        pass
    management.call_command('test')
    sys.exit(0)


if __name__ == "__main__":
    runtests()
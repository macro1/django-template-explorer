"""Test settings file."""
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = "template_explorer_test_secret_key"

INSTALLED_APPS = [
    'tests',
]

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'tests', 'test_template_directory'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

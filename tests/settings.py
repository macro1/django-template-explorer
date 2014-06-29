"""Test settings file."""
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = "template_explorer_test_secret_key"

INSTALLED_APPS = [
    'template_explorer',
    'tests',
]

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'tests', 'test_template_directory'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

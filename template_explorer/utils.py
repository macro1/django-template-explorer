import os
from django.utils.importlib import import_module


def iter_template_dirs_from_settings(settings):
    if 'django.template.loaders.filesystem.Loader' in settings.TEMPLATE_LOADERS:
        for template_dir in settings.TEMPLATE_DIRS:
            yield template_dir
    if 'django.template.loaders.app_directories.Loader' in settings.TEMPLATE_LOADERS:
        for app in settings.INSTALLED_APPS:
            template_dir = os.path.join(os.path.dirname(import_module(app).__file__), 'templates')
            if os.path.isdir(template_dir):
                yield template_dir

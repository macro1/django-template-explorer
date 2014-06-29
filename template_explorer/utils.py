import os
import django
from django.utils.importlib import import_module
from django.template import Template, loader


if django.VERSION < (1, 7):  # pragma: no cover
    # Monkey-patch versions of Django where Template doesn't store origin.
    # See https://code.djangoproject.com/ticket/16096.

    old_template_init = Template.__init__

    def new_template_init(self, template_string, origin=None, name='<Unknown Template>'):
        old_template_init(self, template_string, origin, name)
        self.origin = origin

    Template.__init__ = new_template_init


def iter_template_dirs_from_settings(settings):
    if 'django.template.loaders.filesystem.Loader' in settings.TEMPLATE_LOADERS:
        for template_dir in settings.TEMPLATE_DIRS:
            yield template_dir
    if 'django.template.loaders.app_directories.Loader' in settings.TEMPLATE_LOADERS:
        for app in settings.INSTALLED_APPS:
            template_dir = os.path.join(os.path.dirname(import_module(app).__file__), 'templates')
            if os.path.isdir(template_dir):
                yield template_dir


def iter_templates_from_path(base_path):
    for top, dirs, files in os.walk(base_path):
        for fname in files:
            template_path = os.path.relpath(os.path.join(top, fname), base_path).replace(os.path.sep, "/")
            yield loader.get_template(template_path)

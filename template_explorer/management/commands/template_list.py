import django
from django.template import Template
from django.conf import settings

from ._base import NoArgsCommand
from ... import utils


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        if django.VERSION < (1, 7):  # pragma: no cover
            # Monkey-patch versions of Django where Template doesn't store origin.
            # See https://code.djangoproject.com/ticket/16096.

            old_template_init = Template.__init__

            def new_template_init(self, template_string, origin=None, name='<Unknown Template>'):
                old_template_init(self, template_string, origin, name)
                self.origin = origin

            Template.__init__ = new_template_init
        for template_path in utils.iter_template_dirs_from_settings(settings):
            for template in utils.iter_templates_from_path(template_path):
                self.write(str(template.origin))

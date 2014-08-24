from django.template import Template
from django.core.management import base
import django


def patch_template_init():
    """Monkey-patch for versions of Django where Template doesn't store origin.

    See https://code.djangoproject.com/ticket/16096.
    """
    old_template_init = Template.__init__

    def new_template_init(self, template_string, origin=None, name='<Unknown Template>'):
        old_template_init(self, template_string, origin, name)
        self.origin = origin

    Template.__init__ = new_template_init


class NoArgsCommand(base.NoArgsCommand):

    def write(self, msg):
        if django.VERSION < (1, 5):  # pragma: no cover
            msg += "\n"
        self.stdout.write(msg)

    def execute(self, *args, **options):
        if django.VERSION < (1, 7):  # pragma: no cover
            patch_template_init()
        super(NoArgsCommand, self).execute(*args, **options)

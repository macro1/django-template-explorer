from django.core.management.base import NoArgsCommand
import django
from django.conf import settings

from ... import utils


class Command(NoArgsCommand):

    def write(self, msg):
        if django.VERSION < (1, 5):  # pragma: no cover
            msg += "\n"
        self.stdout.write(msg)

    def handle_noargs(self, **options):
        for template_dir in utils.iter_template_dirs_from_settings(settings):
            self.write(template_dir)

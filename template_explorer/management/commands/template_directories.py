from django.conf import settings

from ._base import NoArgsCommand
from ... import utils


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        for template_dir in utils.iter_template_dirs_from_settings(settings):
            self.write(template_dir)

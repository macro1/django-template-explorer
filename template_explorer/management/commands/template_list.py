from django.conf import settings

from ._base import NoArgsCommand
from ... import utils


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        for template_path in utils.iter_template_dirs_from_settings(settings):
            for template in utils.iter_templates_from_path(template_path):
                self.write(str(template.origin))

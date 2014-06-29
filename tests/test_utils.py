from django.test import TestCase
from template_explorer import utils
from django.conf import settings


class DirsFromSettingsTestCase(TestCase):

    def test_dirs_from_settings(self):
        found_dirs = utils.iter_template_dirs_from_settings(settings)
        for dir in settings.TEMPLATE_DIRS:
            self.assertIn(dir, list(found_dirs))

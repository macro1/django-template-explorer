from copy import deepcopy
import os
from django.test import TestCase
from template_explorer import utils
from django.conf import settings


class DirsFromSettingsTestCase(TestCase):

    def setUp(self):
        self.settings = deepcopy(settings)

    def test_settings_has_filesystem_loader(self):
        self.settings.TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',)
        found_dirs = utils.iter_template_dirs_from_settings(self.settings)
        for dir in settings.TEMPLATE_DIRS:
            self.assertIn(dir, list(found_dirs))

    def test_settings_has_no_filesystem_loader(self):
        self.settings.TEMPLATE_LOADERS = tuple()
        found_dirs = utils.iter_template_dirs_from_settings(self.settings)
        self.assertEqual(list(found_dirs), [])

    def test_settings_has_app_directories_loader(self):
        self.settings.TEMPLATE_LOADERS = ('django.template.loaders.app_directories.Loader',)
        self.settings.INSTALLED_APPS = ('tests',)
        found_dirs = utils.iter_template_dirs_from_settings(self.settings)
        self.assertTrue(next(found_dirs).endswith(os.path.join('tests', 'templates')))

    def test_settings_missing_app_template_directory(self):
        self.settings.TEMPLATE_LOADERS = ('django.template.loaders.app_directories.Loader',)
        self.settings.INSTALLED_APPS = ('tests.no_templates_app',)
        found_dirs = utils.iter_template_dirs_from_settings(self.settings)
        self.assertEqual(list(found_dirs), [])

    def test_settings_has_no_app_directories_loader(self):
        self.settings.TEMPLATE_LOADERS = tuple()
        found_dirs = utils.iter_template_dirs_from_settings(self.settings)
        self.assertEqual(list(found_dirs), [])

import os
from django.test import TestCase
from django.test.utils import override_settings
from django import template
from template_explorer import utils
from django.conf import settings


class DirsFromSettingsTestCase(TestCase):

    @override_settings(TEMPLATE_LOADERS=('django.template.loaders.filesystem.Loader',))
    def test_settings_has_filesystem_loader(self):
        found_dirs = utils.iter_template_dirs_from_settings(settings)
        for template_dir in settings.TEMPLATE_DIRS:
            self.assertIn(template_dir, list(found_dirs))

    @override_settings(TEMPLATE_LOADERS=tuple())
    def test_settings_has_no_filesystem_loader(self):
        found_dirs = utils.iter_template_dirs_from_settings(settings)
        self.assertEqual(list(found_dirs), [])

    @override_settings(TEMPLATE_LOADERS=('django.template.loaders.app_directories.Loader',), INSTALLED_APPS=('tests',))
    def test_settings_has_app_directories_loader(self):
        found_dirs = utils.iter_template_dirs_from_settings(settings)
        self.assertTrue(next(found_dirs).endswith(os.path.join('tests', 'templates')))

    @override_settings(TEMPLATE_LOADERS=('django.template.loaders.app_directories.Loader',),
                       INSTALLED_APPS=('tests.no_templates_app',))
    def test_settings_missing_app_template_directory(self):
        found_dirs = utils.iter_template_dirs_from_settings(settings)
        self.assertEqual(list(found_dirs), [])

    @override_settings(TEMPLATE_LOADERS=tuple())
    def test_settings_has_no_app_directories_loader(self):
        found_dirs = utils.iter_template_dirs_from_settings(settings)
        self.assertEqual(list(found_dirs), [])


class TemplatesInDir(TestCase):

    def test_returns_template(self):
        for t in utils.iter_templates_from_path(settings.TEMPLATE_DIRS[0]):
            self.assertIsInstance(t, template.Template)

    def test_has_origin(self):
        for t in utils.iter_templates_from_path(settings.TEMPLATE_DIRS[0]):
            self.assertTrue(hasattr(t, 'origin'))

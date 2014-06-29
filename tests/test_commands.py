from django.test import TestCase
from django.utils.six.moves import cStringIO as StringIO
from django.core import management
from django.conf import settings


class TestTemplateDirectoryCommand(TestCase):
    command_name = 'template_directories'

    def test_output(self):
        out = StringIO()
        management.call_command(self.command_name, stdout=out)
        self.assertIn("{base_dir}/tests/test_template_directory\n"
                      "{base_dir}/tests/templates".format(base_dir=settings.BASE_DIR), out.getvalue())

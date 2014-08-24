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


class TestTemplateListCommand(TestCase):
    command_name = 'template_list'

    def test_lists_template(self):
        out = StringIO()
        management.call_command(self.command_name, stdout=out)
        self.assertIn("{base_dir}/tests/test_template_directory/base.html".format(base_dir=settings.BASE_DIR),
                      out.getvalue())


class TestTemplateTreeCommand(TestCase):
    command_name = 'template_tree'

    def test_line_count(self):
        out = StringIO()
        management.call_command(self.command_name, stdout=out)
        self.assertEqual(set(out.getvalue().split("\n")), set(["tests/test_template.html", "base.html", ""]))

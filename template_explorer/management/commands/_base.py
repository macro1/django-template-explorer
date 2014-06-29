from django.core.management import base
import django


class NoArgsCommand(base.NoArgsCommand):

    def write(self, msg):
        if django.VERSION < (1, 5):  # pragma: no cover
            msg += "\n"
        self.stdout.write(msg)

import os
import django

__test__ = dict()


if django.VERSION < (1, 6):
    modules = [filename.rsplit('.', 1)[0]
               for filename in os.listdir(os.path.dirname(__file__))
               if filename.endswith('.py') and not filename.startswith('_')]
    for module in modules:
        exec("from .{module} import *".format(module=module))

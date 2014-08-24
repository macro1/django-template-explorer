from collections import defaultdict
from django.conf import settings

from ._base import NoArgsCommand
from ... import utils


class TreeNode(object):

    def __init__(self, name="<No name>", children=None, parent=None):
        self.name = name
        self.children = children or []
        self.parent = parent


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        def write(parent, node, indent=0):
            space = "    " * indent
            if indent == 0:
                self.write(space + parent)
            for child_node in node.children:
                self.write(space + "   |--" + child_node.name)
                if child_node.children:
                    write(child_node.name, child_node, indent + 1)
        child_map = defaultdict(TreeNode)
        from django.template import loader_tags
        for template_path in utils.iter_template_dirs_from_settings(settings):
            for template in utils.iter_templates_from_path(template_path):
                for node in template.nodelist:
                    if isinstance(node, loader_tags.ExtendsNode):
                        child_map[str(node.parent_name.var)].children.append(child_map[template.name])
                        break
                else:
                    child_map[template.name]
        for parent, node in child_map.items():
            node.name = parent
            for child in node.children:
                child.parent = node
        for parent, node in child_map.items():
            if node.parent:
                continue
            write(parent, node)

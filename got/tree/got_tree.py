from treelib import Tree
from .got_node import GotNode
import os
import json
from ..exceptions import CorruptGotException


class GotTree(Tree):
    def create_node(self, *args, parent=None, **kwargs):
        node = GotNode(*args, **kwargs)
        self.add_node(node=node, parent=parent)
        return node

    @property
    def add_commit(self):
        """alias to add a node `commit` to the GotTree"""
        return self.create_node

    def get_commit(self, name_or_hash):
        nodes = list(
            self.filter_nodes(
                lambda n: n.name == name_or_hash or n.hash == name_or_hash
            )
        )
        if len(nodes) > 1:
            raise CorruptGotException(
                "More than one commit with name or hash of {}. Search returned: {}".format(
                    name_or_hash, nodes
                )
            )
        return nodes[0]

    def save(self, src_path):
        got_file = os.path.join(src_path, ".gotfile")
        out = self.to_json(with_data=True)
        with open(got_file, "w") as f:
            f.write(out)

    @classmethod
    def get_tree(cls, src_path):
        got_file = os.path.join(src_path, ".gotfile")
        if os.path.exists(got_file):
            with open(got_file, "r") as f:
                data = json.loads(f.read())
            tree = cls()
            cls._build_tree(data, tree)
        else:
            tree = cls()
        return tree

    @classmethod
    def get_tree(cls, src_path):
        got_file = os.path.join(src_path, ".gotfile")
        if os.path.exists(got_file):
            with open(got_file, "r") as f:
                data = json.loads(f.read())
            tree = cls()
            cls._build_tree(data, tree)
        else:
            tree = cls()
        return tree

    @classmethod
    def _build_tree(cls, node, tree, parent=None):
        name = list(node.keys())[0]
        child_properties = node[name]
        data = child_properties["data"]
        tree.create_node(identifier=name, data=data, parent=parent, tag=data["name"])
        if "children" in child_properties:
            for child in child_properties["children"]:
                cls._build_tree(child, tree, name)

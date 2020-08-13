from treelib import Tree
import os
import json


class GotTree(Tree):
    def __init__(self, current_node=None):
        self.current_node = current_node

    def save(self, src_path):
        got_file = os.path.join(src_path, ".gotfile")
        out = self.to_json(with_data=True)
        with open(got_file, "w") as f:
            f.write(out)

    @classmethod
    def get_tree(src_path):
        got_file = os.path.join(src_path, ".gotfile")
        if os.path.exists(got_file):
            with open(got_file, "r") as f:
                data = json.loads(f.read())
            tree = GotTree()
            GotTree._build_tree(data, tree)
        else:
            tree = GotTree()
        return tree

    @staticmethod
    def _build_tree(node, tree, parent=None):
        name = list(node.keys())[0]
        child_properties = node[name]
        data = child_properties["data"]
        tree.create_node(identifier=name, data=data, parent=parent)
        if "children" in child_properties:
            for child in child_properties["children"]:
                GotTree._build_tree(child, tree, name)

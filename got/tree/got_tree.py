from treelib import Tree
import os
import pickle


class GotTree(Tree):
    def __init__(self, current_node=None):
        self.current_node = current_node

    def save(self, src_path):
        got_file = os.path.join(src_path, ".gotfile")
        with open(got_file, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def get_tree(src_path):
        got_file = os.path.join(src_path, ".gotfile")
        if os.path.exists(got_file):
            with open(got_file, "rb") as f:
                tree = pickle.load(f)
        else:
            tree = GotTree()
        return tree

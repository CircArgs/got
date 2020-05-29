import os
import shutil
import argparse


class Init(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        path = os.getcwd()
        os.system("git init")
        with open(".git/.gitignore", "w") as gitignore:
            gitignore.write("*")
        shutil.move(".git", os.path.join(path, ".got"))

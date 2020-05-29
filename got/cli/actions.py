import os
import shutil
import argparse


class Init(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print(parser)
        print(namespace)
        print(values)
        print(os.getcwd())
        os.system("git init got_temp")
        with open(os.path.join("got_temp", ".git", ".gitignore"), "w") as gitignore:
            gitignore.write("*")
        os.rename(os.path.join("got_temp", ".git"),
                  os.path.join("got_temp", ".got"))
        shutil.move(os.path.join("got_temp", ".got"),
                    os.path.dirname(os.path.abspath("got_temp")))
        shutil.rmtree("got_temp")

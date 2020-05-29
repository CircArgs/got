# https://cleo.readthedocs.io/en/latest/
import os
import shutil
from cleo import Command


class Init(Command):
    """
    Instantiates Got

    init
    """

    def handle(self):
        os.system("git init got_temp")
        with open(os.path.join("got_temp", ".git", ".gitignore"), "w") as gitignore:
            gitignore.write("*")
        os.rename(os.path.join("got_temp", ".git"), os.path.join("got_temp", ".got"))
        shutil.move(
            os.path.join("got_temp", ".got"),
            os.path.dirname(os.path.abspath("got_temp")),
        )
        shutil.rmtree("got_temp")
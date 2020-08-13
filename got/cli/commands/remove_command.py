# https://cleo.readthedocs.io/en/latest/
import os
import shutil
from cleo import Command
from ...utils import is_got, nukedir


class Remove(Command):
    """
    Removes Got

    remove
        {path? : path which .got is located in - default cwd}
        {--f|force : attempt to forcibly remove the .got}
    """

    def handle(self):
        path = self.argument("path")
        if not path:
            path = os.getcwd()
        path = is_got(path)
        force = self.option("force")
        if force:
            nukedir(path)
        else:
            shutil.rmtree(path)

import os
import shutil
from .got_base_command import GotCommand
from ...utils import is_got, nukedir


class Remove(GotCommand):
    """
    Removes Got

    remove
        {--p|path=.} : path which .got is located in - default cwd}
        {--f|force : attempt to forcibly remove the .got}
    """

    def handle(self):
        path = self.option("path")
        if path == ".":
            path = os.getcwd()
        path = is_got(path)
        force = self.option("force")
        if force:
            nukedir(path)
        else:
            shutil.rmtree(path)

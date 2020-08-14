import os
from cleo import Command
from got.service import Got
from got.utils import is_got


class Start(Command):
    """
    Start got

    start
        {--B|no-shell : If set, got will not enter shell mode}
        {--p|path=. : path which .got is located in - default cwd}
        {--ignore-untracked : do not add untracked files on start}
    """

    def handle(self):
        background = self.option("no-shell")
        path = self.option("path")
        if path == ".":
            path = os.getcwd()
        ignore_untracked = self.option("ignore-untracked")
        path = os.path.abspath(path)
        got = Got(path, interactive=not background, ignore_untracked=ignore_untracked)
        got.run()

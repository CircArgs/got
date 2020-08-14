# https://cleo.readthedocs.io/en/latest/
import os
import shutil
from cleo import Command
from ...macros import GIT


class Git(Command):
    """
    Explicitly use git in got

    git
        {git* : git command to execute on got repo}
        {--p|path=.} : path which .got is located in - default cwd}
    """

    def handle(self):
        path = self.option("path")
        if path == ".":
            path = os.getcwd()
        git_command = " ".join(self.argument("git"))
        GIT(git_command, git_quiet=False, cwd=path)

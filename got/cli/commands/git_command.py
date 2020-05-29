# https://cleo.readthedocs.io/en/latest/
import os
import shutil
from cleo import Command
from ...macros import GIT


class Git(Command):
    """
    Use git in got

    git
        {git* : git command to execute on got repo}
    """

    def handle(self):

        git_command = " ".join(self.argument("git"))
        print(git_command)
        GIT(git_command, False, True)

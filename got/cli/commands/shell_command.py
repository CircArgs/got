# https://cleo.readthedocs.io/en/latest/
import os
import shutil
from cleo import Command
from ...macros import SHELL
from shlex import split


class Shell(Command):
    """
    Explicitly pass commands to the shell

    shell
        {shell* : shell command to forward}
    """

    def handle(self):
        shell_command = " ".join(self.argument("shell"))
        return SHELL(shell_command)

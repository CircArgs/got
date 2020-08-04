# https://cleo.readthedocs.io/en/latest/
import os
import shutil
from cleo import Command
from ...macros import SHELL
from shlex import split


class Shell(Command):
    """
    Shell command passthrough

    shell
        {shell* : shell command to forward}
    """

    def handle(self):
        shell_command = " ".join(self.argument("git"))
        SHELL(shell_command)

# https://cleo.readthedocs.io/en/latest/
import os
import shutil
from .got_base_command import GotCommand
from ...macros import SHELL
from shlex import split


class Shell(GotCommand):
    """
    Explicitly pass commands to the shell

    shell
        {shell* : shell command to forward}
    """

    def handle(self):
        shell_command = " ".join(self.argument("shell"))
        return SHELL(shell_command)

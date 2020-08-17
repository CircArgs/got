# https://cleo.readthedocs.io/en/latest/
import os
import subprocess
import shutil
from .got_base_command import GotCommand
from ...utils import is_got, remove_got, nukedir
from ...exceptions import NotGotException
from ...macros import SHELL


class Init(GotCommand):
    """
    Instantiates Got

    init
        {--y|yes : If set, respond `yes` to all possible prompts.}
        {--p|path=.} : path which .got is located in - default cwd}
    """

    def handle(self):
        yes = self.option("yes")
        move_to = self.option("path")
        if move_to == ".":
            move_to = os.getcwd()

        try:
            self.line("<info>Checking for existing got dir</info>")
            is_got(move_to)
            if not (
                yes
                or (
                    self.line("<warning>{} already contains .got. </>".format(move_to))
                    or self.confirm("Would you like to overwrite it?", False)
                )
            ):
                self.line("<error>Failed to instantiate got dir.</error>")
                return
            else:
                self.line("<warning>Removing got {}.</>".format(move_to))
                remove_got(move_to)
        except NotGotException:
            self.line("<info>No existing got dir. Instantiating new got dir</info>")
        init_res = SHELL("git init -q __got_temp__", cwd=move_to, exit=False)
        got_temp = os.path.join(move_to, "__got_temp__")
        if init_res:
            self.line(
                "<error>Could not use git. Failed to instantiate got dir.</error>"
            )
        with open(os.path.join(got_temp, ".git", ".gitignore"), "w") as gitignore:
            gitignore.write("/*")
        os.rename(
            os.path.join(got_temp, ".git"), os.path.join(got_temp, ".got"),
        )
        shutil.move(
            os.path.join(got_temp, ".got"), move_to,
        )
        nukedir(got_temp)
        self.line(
            "<success>Initialized empty Got repository in {} 🤩</success>".format(
                os.path.join(move_to, ".got")
            )
        )

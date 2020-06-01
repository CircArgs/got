# https://cleo.readthedocs.io/en/latest/
import os
import subprocess
import shutil
from cleo import Command
from colorama import Fore
from ...utils import is_got, remove_got


class Init(Command):
    """
    Instantiates Got

    init
        {--y|yes : If set, respond `yes` to all possible prompts.}
    """

    def handle(self):
        yes = self.option("yes")
        self.add_style("success", fg="blue", bg="green", options=["bold", "blink"])
        self.line("<comment>Checking for existing got dir</comment>")
        move_to = os.path.dirname(os.path.abspath("__got_temp__"))
        if is_got(move_to):
            if not (
                yes
                or self.confirm(
                    Fore.LIGHTRED_EX
                    + "{} already contains .got. Would you like to overwrite it?".format(
                        move_to
                    ),
                    False,
                )
            ):
                self.line("<error>Failed to instantiate got dir.</error>")
                return
            else:
                self.line(Fore.LIGHTYELLOW_EX + "Removing got {}.".format(move_to))
                remove_got(move_to)
        else:
            self.line("<info>No existing got dir. Instantiating new got dir</info>")
        init_res = subprocess.run(
            ["git", "init", "-q", "__got_temp__"], capture_output=True
        )
        if init_res.returncode:
            self.line(
                "<error>Could not use git. Failed to instantiate got dir.</error>"
            )
        with open(os.path.join("__got_temp__", ".git", ".gitignore"), "w") as gitignore:
            gitignore.write("*\n*/")
        os.rename(
            os.path.join("__got_temp__", ".git"), os.path.join("__got_temp__", ".got")
        )
        shutil.move(
            os.path.join("__got_temp__", ".got"), move_to,
        )
        shutil.rmtree("__got_temp__")
        self.line(
            "<success>🤩 Initialized empty Got repository in {}</success>".format(
                os.path.join(move_to, ".got")
            )
        )

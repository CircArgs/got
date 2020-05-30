# https://cleo.readthedocs.io/en/latest/
import os
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
        move_to = os.path.dirname(os.path.abspath("got_temp"))
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
        os.system("git init -q got_temp")
        with open(os.path.join("got_temp", ".git", ".gitignore"), "w") as gitignore:
            gitignore.write("*")
        os.rename(os.path.join("got_temp", ".git"), os.path.join("got_temp", ".got"))
        shutil.move(
            os.path.join("got_temp", ".got"), move_to,
        )
        shutil.rmtree("got_temp")
        self.line(
            "<success>Initialized empty Got repository in {}</success>".format(
                os.path.join(move_to, ".got")
            )
        )

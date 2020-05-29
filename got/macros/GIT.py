import os
from colorama import Fore
from ..utils import is_got

# BUG: quiet flag not working


def GIT(cmd, git_quiet=True, show=False):
    if not is_got():
        print(Fore.RED + "Not a got repository (or any of the parent directories).")
    else:
        to_exec = "git {} --git-dir=.got {}".format("--quiet" if git_quiet else "", cmd)
        if show:
            print(to_exec)
        os.system(to_exec)

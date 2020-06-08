import os
from colorama import Fore
from got.utils import is_got


def GIT(cmd, git_quiet=False, show=False, exec=True, remove_lock=True):
    if not is_got():
        print(Fore.RED + "Not a got repository (or any of the parent directories).")
    else:
        if remove_lock and os.path.exists(".got/index.lock"):
            os.remove(".got/index.lock")
        to_exec = "git --git-dir=.got {} {}".format(cmd, "--quiet" if git_quiet else "")
        if show:
            print(to_exec)
        if exec:
            os.system(to_exec)
        return to_exec

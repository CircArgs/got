import os
import subprocess
from colorama import Fore
from got.utils import is_got


def GIT(cmd, git_quiet=False, show=False, exec=True, remove_lock=True):
    if type(cmd) != list:
        cmd = [cmd]
    if not is_got():
        print(Fore.RED + "Not a got repository (or any of the parent directories).")
    else:
        if remove_lock and os.path.exists(".got/index.lock"):
            os.remove(".got/index.lock")
        to_exec = " && ".join(
            [
                "git --git-dir=.got {}{}".format(
                    command, " --quiet" if git_quiet else ""
                )
                for command in cmd
            ]
        )
        if show:
            print(to_exec)
        if exec:
            p = subprocess.Popen(to_exec, stdout=subprocess.PIPE, shell=True)
            return tuple(
                (None if v is None else v.decode("utf-8")) for v in p.communicate()
            )
        return to_exec

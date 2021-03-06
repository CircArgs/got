import os
import subprocess
from colorama import Fore
from got.utils import is_got
from ..exceptions import GitNoSuchCommandException, NotGotException
from ..cli import cli


def GIT(
    cmd,
    git_quiet=False,
    print_command=False,
    print_output=True,
    exec=True,
    remove_lock=True,
    send=None,
    cwd=os.getcwd(),
    got_path=".got",
):
    if type(cmd) != list:
        cmd = [cmd]
    if not is_got():
        cli.io.write_line(
            "<error>Not a got repository (or any of the parent directories).</>"
        )
        raise NotGotException()
    else:
        if remove_lock and os.path.exists(".got/index.lock"):
            os.remove(".got/index.lock")
        to_exec = " && ".join(
            [
                "git --git-dir={} {}{}".format(
                    got_path, command, " --quiet" if git_quiet else ""
                )
                for command in cmd
            ]
        )
        if print_command:
            cli.io.write_line(to_exec)
        if exec:
            if send is None:
                p = subprocess.Popen(
                    to_exec,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True,
                    cwd=cwd,
                )

                out, err = tuple(
                    (None if v is None else v.decode("utf-8")) for v in p.communicate()
                )
                if (not err is None) and ("not a git command" in err):
                    raise GitNoSuchCommandException()
                if print_output and (not err is None) and out:
                    cli.io.write_line(out)
                return out, err
            else:
                send(to_exec)
        return to_exec

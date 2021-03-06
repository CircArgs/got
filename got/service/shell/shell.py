import collections
import contextlib
import os
import signal
import subprocess
import sys
import pexpect
from vistir.contextmanagers import temp_environ
from vistir.compat import Path, get_terminal_size
from clikit.api.command.exceptions import NoSuchCommandException
from ...exceptions import GitNoSuchCommandException, NotGotException
import shlex
from ...macros import GIT
from ...utils import get_shell
from ...cli import cli


class Shell:
    def __init__(self, src_path):
        # Grab current terminal dimensions to replace the hardcoded default
        # dimensions of pexpect.
        self.src_path = src_path

        dims = get_terminal_size()
        name, executable = get_shell()
        self.reset_buffer()
        with temp_environ():
            self.c = pexpect.spawn(
                executable, ["-i"], dimensions=(dims.lines, dims.columns)
            )

        # Handler for terminal resizing events
        # Must be defined here to have the shell process in its context, since
        # we can't pass it as an argument
        def sigwinch_passthrough(sig, data):
            dims = get_terminal_size()
            self.c.setwinsize(dims.lines, dims.columns)

        signal.signal(signal.SIGWINCH, sigwinch_passthrough)

        # Interact with the new shell.
        self.c.interact(
            escape_character=None, input_filter=self.in_intercept,
        )
        self.c.close()
        sys.exit(self.c.exitstatus)

    def in_intercept(self, entered):
        ret = entered
        entered = entered.decode("utf-8")

        if entered != "\r":
            self.buffer += entered
            return ret
        else:
            self.route()
            return "".encode("utf-8")

    def send_overwrite(self, cmd=""):
        self.c.sendline("\x08" * len(self.buffer) + cmd)

    def reset_buffer(self):
        self.buffer = ""

    def route(self):
        cmd = self.buffer.strip()
        if cmd.strip():
            name, *args = shlex.split(cmd)

            if name == "shell":
                self.send_overwrite(cmd[len("shell") :])
            if name == "git":
                git_cmd = GIT(
                    cmd[len("git") :],
                    exec=False,
                    got_path=os.path.join(self.src_path, ".got"),
                )
                self.send_overwrite(git_cmd)
            else:
                try:
                    got_name, got_args = name, args
                    if name.strip() == "got":
                        got_name, *got_args = shlex.split(cmd[3:])
                    command = cli.application.find(got_name)
                    command.call(got_name, got_args)
                    self.send_overwrite()
                except NoSuchCommandException:
                    self.c.sendline()
        else:
            self.c.sendline()

        self.reset_buffer()

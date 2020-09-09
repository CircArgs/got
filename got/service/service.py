# https://blog.magrathealabs.com/filesystem-events-monitoring-with-python-9f5329b651c3


import sys
import shlex
import os
import pickle
import time
from watchdog.observers import Observer
from got.events import GotHandler
from ..cli import cli
from got.__version__ import version
from clikit.api.command.exceptions import NoSuchCommandException
from got.graph import GotGraph
from ..exceptions import GitNoSuchCommandException, NotGotException
from ..utils import (
    lines as ascii_got_lines,
    width as ascii_got_width,
    get_shell,
    is_got,
    got_lock,
)
from .shell import Shell


class Got:
    def __init__(self, src_path, ignore_untracked, interactive=False, application=None):
        self.src_path = src_path
        self.got_path = is_got(src_path)
        self.interactive = interactive
        self.got_ignore = ["*/.git/*", "*/.got/*"]
        # got_lock(src_path)
        got_ignore_path = os.path.join(self.got_path, ".gotignore")
        if os.path.exists(got_ignore_path):
            with open(got_ignore_path) as got_ignore:
                self.got_ignore += ["*/" + l for l in got_ignore.readlines()]
        self.application = application
        self.application.got = self
        self.__op_path = os.getcwd()

        self.graph = GotGraph(self.got_path)

        self.__event_handler = GotHandler(
            self.src_path,
            self.got_path,
            self.got_ignore,
            got_graph=self.graph,
            ignore_untracked=ignore_untracked,
        )

        self.__event_observer = Observer()

    def run(self):
        self.start()
        if self.interactive:
            # intro for repl
            repl_intro = ""
            version_statement = "The got repl. VERSION {}".format(version)
            pad = int(abs(len(version_statement) - ascii_got_width) / 2) * " "
            if len(version_statement) > ascii_got_width:
                for line in ascii_got_lines:
                    repl_intro += pad + line + pad + "\n"
                repl_intro += version_statement + "\n"
            else:
                repl_intro += "\n".join(ascii_got_lines)
                repl_intro += pad + version_statement + pad + "\n"

            cli.io.write_line("<bc1>" + repl_intro + "</>")
            # enter user interact with child shell
            Shell(self.src_path)
            # shell exit -> stop got
            self.stop()
        else:
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()
        os.environ["GOT_ACTIVE"] = "1"

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()
        os.environ["GOT_ACTIVE"] = "0"

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler, self.__op_path, recursive=True
        )


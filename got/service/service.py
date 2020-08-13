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
from got.tree import GotTree, GotNode
from ..exceptions import GitNoSuchCommandException, NotGotException
from ..utils import (
    lines as ascii_got_lines,
    width as ascii_got_width,
    get_shell,
    is_got,
    got_lock,
)
from .shell.shell import Shell


class Got:
    def __init__(self, src_path, interactive=False):
        self.got_ignore = ["*/.git/*", "*/.got/*"]
        got_path = is_got(src_path)
        # got_lock(src_path)
        got_ignore_path = os.path.join(got_path, ".gotignore")
        if os.path.exists(got_ignore_path):
            with open(got_ignore_path) as got_ignore:
                self.got_ignore += ["*/" + l for l in got_ignore.readlines()]
        self.interactive = interactive
        self.tree = None
        self.__src_path = src_path
        self.__got_tree()

        self.__event_handler = GotHandler(self.got_ignore)
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
            Shell()
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

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler, self.__src_path, recursive=True
        )

    def __got_tree(self):
        if self.tree is None:
            self.tree = Got.get_got_tree(self.__src_path)
        return self.tree

    def get_got_tree(self):
        return None

    def commit(self, name, hash):
        self.tree.create_node(name, hash, parent=self.tree.current_node)
        Got.save_got_tree(self.__src_path, self.tree)

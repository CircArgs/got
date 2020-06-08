# https://blog.magrathealabs.com/filesystem-events-monitoring-with-python-9f5329b651c3


import sys
import os
import pickle
import time
from watchdog.observers import Observer
from colorama import Fore, Back
from got.events import GotHandler
from got.cli import cli
from got.__version__ import version
from clikit.api.command.exceptions import NoSuchCommandException
from treelib import Tree, Node


class Got:
    def __init__(self, src_path, interactive=False):
        self.got_ignore = ["*/.git/*", "*/.got/*"]
        got_ignore_path = os.path.join(src_path, ".gotignore")
        if os.path.exists(got_ignore_path):
            with open(got_ignore_path) as got_ignore:
                self.got_ignore += ["*/" + l for l in got_ignore.readlines()]
        self.interactive = interactive
        got_file = os.path.join(src_path, ".gotfile")
        if os.path.exists(got_file):
            with open(got_file, "rb") as f:
                tree = pickle.load(f)
        else:
            tree = Tree()
        self.__src_path = src_path
        self.__event_handler = GotHandler(self.got_ignore)
        self.__event_observer = Observer()

    def run(self, interactive=False):

        self.start()
        # intro for repl
        if self.interactive:
            repl_intro = "The got repl. VERSION {}".format(version)
            print("=" * len(repl_intro) + "\n")
            print(repl_intro)
            print("\n" + "=" * len(repl_intro) + "\n")
        try:
            while True:
                # not repl
                if not self.interactive:
                    time.sleep(1)
                else:  # repl
                    print(Fore.MAGENTA + "got: ", end="")
                    # get user input
                    cmd = input().strip()
                    # repl exit commands
                    if cmd in ("quit", "q"):
                        return
                    cmd = cmd.split(" ")
                    # command name is first
                    name, args = cmd[0], " ".join(cmd[1:])
                    # no command entered skip
                    if not name:
                        continue
                    command = None
                    try:
                        command = cli.application.find(name)
                    except NoSuchCommandException as e:
                        print(Fore.RED + str(e))
                    if not command is None:
                        try:
                            command.call(name, args)
                        except Exception as e:
                            print(
                                Fore.RED
                                + "There was an error processing your command `{}`. The error emitted by the command was:".format(
                                    name
                                )
                            )
                            print(Fore.LIGHTRED_EX + Back.LIGHTWHITE_EX + str(e))

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

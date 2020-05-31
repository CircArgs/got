# https://blog.magrathealabs.com/filesystem-events-monitoring-with-python-9f5329b651c3


import sys
import os
import time
from watchdog.observers import Observer
from colorama import Fore
from got.events import GotHandler
from got.cli import cli
from cleo import CommandTester
import fnmatch


class Got:
    def __init__(self, src_path, interactive=False):
        got_ignore = [".git"]
        got_ignore_path = os.path.join(src_path, ".gotignore")
        if os.path.exists(got_ignore_path):
            with open(got_ignore_path) as got_ignore:
                got_ignore += got_ignore.readlines()
        self.got_ignore = list(map(fnmatch.translate, got_ignore))
        self.interactive = interactive
        self.__src_path = src_path
        self.__event_handler = GotHandler(self.got_ignore)
        self.__event_observer = Observer()

    def run(self, interactive=False):

        self.start()
        try:
            while True:
                if not self.interactive:
                    time.sleep(1)
                else:
                    print("got: ", end="")
                    cmd = input()
                    if cmd in ("quit", "q"):
                        return
                    cmd = cmd.split(" ")
                    name, args = cmd[0], " ".join(cmd[1:])
                    try:
                        command = cli.application.find(name)
                    except:
                        pass
                    if command:
                        command = CommandTester(command)
                        command.execute(args)
                    

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

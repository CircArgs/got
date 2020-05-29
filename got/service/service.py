# https://blog.magrathealabs.com/filesystem-events-monitoring-with-python-9f5329b651c3


import sys
import os
import time
from watchdog.observers import Observer
from ..events import GotHandler
import fnmatch


class Got:
    def __init__(self, src_path):
        with open(os.path.join(src_path, ".gotignore")) as got_ignore:
            got_ignore = got_ignore.readlines()
            got_ignore = list(map(fnmatch.translate, got_ignore))
        self.__src_path = src_path
        self.__event_handler = GotHandler(got_ignore)
        self.__event_observer = Observer()

    def run(self):
        self.start()
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

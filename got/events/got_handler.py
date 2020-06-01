import os
from got.macros import GIT
from watchdog.events import RegexMatchingEventHandler


class GotHandler(RegexMatchingEventHandler):
    def __init__(self, got_ignore):
        self.got_ignore = got_ignore
        super().__init__(ignore_regexes=self.got_ignore)

    def on_modified(self, event):
        print(event)
        # self.process(event)

    def process(self, event):
        cmd = GIT("add {}".format(event.src_path), exec=False)
        cmd += " && "
        cmd += GIT('commit -m "modified file {}"'.format(event.src_path), exec=False)
        os.system(cmd)

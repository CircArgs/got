import os
from got.macros import GIT
from watchdog.events import PatternMatchingEventHandler


class GotHandler(PatternMatchingEventHandler):
    def __init__(self, got_ignore):
        print(got_ignore)
        self.got_ignore = got_ignore
        super().__init__(ignore_patterns=self.got_ignore, ignore_directories=True)

    def on_any_event(self, event):
        self.process(event)

    def process(self, event):
        cmd = GIT("add {}".format(event.src_path), exec=False)
        cmd += " && "
        cmd += GIT('commit -m "modified file {}"'.format(event.src_path), exec=False)
        os.system(cmd)

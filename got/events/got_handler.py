import os
from got.macros import GIT
from watchdog.events import PatternMatchingEventHandler
from got.utils.got_head import got_head


class GotHandler(PatternMatchingEventHandler):
    def __init__(self, got_ignore):
        print(got_ignore)
        self.got_ignore = got_ignore
        super().__init__(ignore_patterns=self.got_ignore, ignore_directories=True)

    def on_any_event(self, event):
        self.process(event)

    def process(self, event):
        cmd = [
            "add {}".format(event.src_path),
            'commit -m "modified file {}"'.format(event.src_path),
        ]
        out, err = GIT(cmd)
        if err is None:
            head = got_head()

import os

from got.macros import GIT
from watchdog.events import PatternMatchingEventHandler
from got.utils.got_head import got_head
from ..cli import cli
from ..exceptions import GotCommitException


class StartEvent:
    def __init__(self, src_path):
        self.src_path = src_path


class GotHandler(PatternMatchingEventHandler):
    def __init__(self, src_path, got_path, got_ignore, got_graph, ignore_untracked):
        self.got_ignore = got_ignore
        self.got_path = got_path
        self.got_graph = got_graph
        self.commit(StartEvent(src_path), ["started Got"])
        super().__init__(ignore_patterns=self.got_ignore, ignore_directories=True)

    def on_created(self, event):
        msgs = ["created file {}.".format(event.src_path)]
        self.commit(event, msgs)

    def on_modified(self, event):
        msgs = ["modified file {}.".format(event.src_path)]
        self.commit(event, msgs)

    def on_moved(self, event):
        msgs = ["moved file {}.".format(event.src_path)]
        self.commit(event, msgs)

    def on_deleted(self, event):
        msgs = ["deleted file {}.".format(event.src_path)]
        self.commit(event, msgs)

    def commit(self, event, msgs):
        msgs = [' -m "{}"'.format(msg) for msg in msgs]
        msg = "".join(msgs)
        cmds = [
            "add {}".format(event.src_path),
            "commit {}".format(msg),
        ]
        out, err = GIT(cmds, print_output=False, got_path=self.got_path)
        if err.strip():
            raise GotCommitException(err)
        else:
            self.got_graph.commit()

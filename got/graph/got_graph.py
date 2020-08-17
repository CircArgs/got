from git_networkx import GitNX, Commit, LocalBranch, LocalHead
import os
from inspect import ismethod
from ..exceptions import CorruptGotException


class GotGraph:
    def __init__(self, got_path):
        self.got_path = got_path
        self.reload()

    def commit(self, *args, **kwargs):
        self.reload()

    def reload(self, got_path=None):
        if not got_path is None:
            self.got_path = got_path
        self.graph = GitNX(self.got_path, "lch")


import os
from distutils.util import strtobool
from .got_base_command import GotCommand
from got.service import Got
from got.utils import is_got


class Start(GotCommand):
    """
    Start got

    start
        {--B|no-shell : If set, got will not enter shell mode}
        {--p|path=. : path which .got is located in - default cwd}
        {--ignore-untracked : do not add untracked files on start}
    """

    def handle(self):

        got_activated = strtobool(os.environ.get("GOT_ACTIVE", "0"))
        if got_activated:
            self.line("<info>You are already running Got</>")

            return

        # Setting this to avoid spawning unnecessary nested shells
        os.environ["GOT_ACTIVE"] = "1"

        background = self.option("no-shell")

        path = self.option("path")
        if path == ".":
            path = os.getcwd()
        ignore_untracked = self.option("ignore-untracked")
        path = os.path.abspath(path)
        got = Got(
            path,
            interactive=not background,
            ignore_untracked=ignore_untracked,
            application=self.application,
        )
        got.run()

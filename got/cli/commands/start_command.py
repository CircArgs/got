import os
from cleo import Command
from got.service import Got
from got.utils import is_got


class Start(Command):
    """
    Start got

    start
        {--B|no-shell : If set, got will not enter shell mode}
    """

    def handle(self):
        background = self.option("no-shell")
        got = Got(os.getcwd(), interactive=not background)
        got.run()

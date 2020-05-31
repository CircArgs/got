import os
from cleo import Command
from ...service import Got
from ...utils import is_got


class Start(Command):
    """
    Start got

    start
        {--i|interactive : If set, got will run in repl mode, else it will run in the background}
    """

    def handle(self):
        if not is_got():
            self.line(
                "<error>Can only run Got from a got directory. Try running `got init`</error>"
            )
            return
        interactive = self.option("interactive")
        got = Got(os.getcwd(), interactive=interactive)
        if not interactive:
            target = got.run
        else:
            got.run()

import os
from distutils.util import strtobool
from cleo import Command


class GotCommand(Command):
    def __init__(self, *args, **kwargs):
        super(GotCommand, self).__init__(*args, **kwargs)

    @property
    def interactive(self):
        return bool(
            strtobool(os.environ.get("GOT_ACTIVE", "0")) or bool(self.application.got)
        )


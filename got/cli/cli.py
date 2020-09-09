import os
from distutils.util import strtobool
from .commands import GotCommand, Init, Git, Shell, Start, Remove, Undo
from got.__version__ import version
from cleo import Application as BaseApplication
from .config import GotAppConfig
from .got_io import GotIO


class Application(BaseApplication):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.interactive = strtobool(os.environ.get("GOT_ACTIVE", "0"))
        self.got = None
        self.fart = "poo"


config = GotAppConfig("got", version)
io = GotIO(config.default_style_set)
application = Application("got", complete=True, config=config)
application.add(Init())
application.add(Git())
application.add(Shell())
application.add(Start())
application.add(Remove())
application.add(Undo())


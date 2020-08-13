from .commands import Init, Git, Shell, Start, Remove
from got.__version__ import version
from cleo import Application
from .config import GotAppConfig
from .got_io import GotIO

config = GotAppConfig()
config.set_version(version)
io = GotIO(config.default_style_set)
application = Application("got", complete=True, config=config)
application.add(Init())
application.add(Git())
application.add(Shell())
application.add(Start())
application.add(Remove())

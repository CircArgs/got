from .commands import Init
from cleo import Application

application = Application()
application.add(Init())

from .commands import Init, Git
from cleo import Application

application = Application("Got. Commiting often. \n got it?", complete=True)
application.add(Init())
application.add(Git())

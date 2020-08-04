from .commands import Init, Git, Shell, Start
from cleo import Application

application = Application("Got. Commiting often. got it?", complete=True)
application.add(Init())
application.add(Git())
application.add(Shell())
application.add(Start())

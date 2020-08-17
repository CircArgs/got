import os
from .got_base_command import GotCommand
from got.service import Got
from got.utils import is_got


class Undo(GotCommand):
    """
    Move to a previous got node

    undo
    
    """

    def handle(self):
        print(self._application.interactive)

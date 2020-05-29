import os
import shutil
from . import is_got


def remove_got(path=os.getcwd()):
    exists = is_got(path)
    if exists:
        shutil.rmtree(exists)

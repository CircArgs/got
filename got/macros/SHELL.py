import os
import sys
import subprocess
from ..utils import get_shell
from ..cli import cli


def SHELL(cmd, cwd=os.getcwd(), exit=True):
    code = subprocess.run([get_shell()[1], "-i", "-c", cmd], cwd=cwd).returncode
    if code == 0:
        if exit:
            sys.exit(0)
        else:
            return code
    else:
        code = subprocess.run(cmd, cwd=cwd, shell=True).returncode
        if code == 0:
            if exit:
                sys.exit(0)
            else:
                return code

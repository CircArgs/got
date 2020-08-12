import os
import sys
import subprocess
from ..utils import get_shell
from ..cli import cli


def SHELL(cmd):
    code = subprocess.run([get_shell()[1], "-i", "-c", cmd]).returncode
    if code == 0:
        sys.exit(0)
    sys.exit(subprocess.run(cmd, shell=True).returncode)

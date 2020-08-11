import os
import subprocess
from shellingham import detect_shell, ShellDetectionFailure


def SHELL(cmd):
    try:
        shell = detect_shell()[1]
    except ShellDetectionFailure:
        shell = None
    code = subprocess.call(cmd, executable=shell, shell=True)
    if code != 0:
        raise Exception(
            "Process command `{}` exited with nonzero exit code {}".format(cmd, code)
        )


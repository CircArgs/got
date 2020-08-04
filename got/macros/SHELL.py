import os
import subprocess


def SHELL(cmd):
    code = subprocess.call(cmd, shell=True)
    if code != 0:
        raise Exception(
            "Process command `{}` exited with nonzero exit code {}".format(cmd, code)
        )


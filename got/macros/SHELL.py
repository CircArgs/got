import os
import subprocess


def SHELL(cmd):
    p = subprocess.call(cmd, shell=True)


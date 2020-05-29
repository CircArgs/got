import os


def GIT(cmd):
    os.system("git --git-dir=.got {}".format(cmd))

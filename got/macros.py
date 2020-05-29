import os


def GIT(cmd):
    os.system("git -q --git-dir=.got {}".format(cmd))

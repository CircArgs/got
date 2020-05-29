import os


def GIT(cmd, git_quiet=True, show=False):
    to_exec = "git {} --git-dir=.got {}".format("-q" if git_quiet else "", cmd)
    if show:
        print(to_exec)
    os.system(to_exec)

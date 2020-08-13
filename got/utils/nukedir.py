# https://stackoverflow.com/a/13766571/7907717
import os


def nukedir(dir):
    if dir[-1] == os.sep:
        dir = dir[:-1]
    files = os.listdir(dir)
    for file in files:
        if file == "." or file == "..":
            continue
        path = dir + os.sep + file
        if os.path.isdir(path):
            nukedir(path)
        else:
            os.unlink(path)
    os.rmdir(dir)

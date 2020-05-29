import os
import shutil


def prep(path):
    os.system("git init")
    with open(".git/.gitignore", "w") as gitignore:
        gitignore.write("*")
    shutil.move(".git", os.path.join(path, ".got"))

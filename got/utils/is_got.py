import os


def is_got(path=os.getcwd()):
    potential_path = os.path.join(path, ".got")
    if os.path.exists(potential_path):
        return potential_path
    else:
        return False

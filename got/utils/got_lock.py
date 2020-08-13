import os
from .is_got import is_got
from ..exceptions import GotLockedException


def lockfile_path(base):
    return os.path.join(base, "got.lock")


def is_got_locked(path=os.getcwd()):
    base = is_got(path)
    lockfile = lockfile_path(base)
    return os.path.exists(lockfile) and lockfile


def got_lock(path=os.getcwd()):
    """
    gets a lock on got
    """
    base = is_got(path)
    lockfile = lockfile_path(base)
    try:
        with open(lockfile, "x") as f:
            f.write("")
    except FileExistsError:
        raise GotLockedException(
            "The got directory at {} is locked. This or another process may be operating on got.".format(
                base
            )
        )


def remove_got_lock(path=os.getcwd()):
    locked = is_got_locked(path)
    if locked:
        os.remove(locked)

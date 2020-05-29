import argparse
from .actions import Init


def command():
    parser = argparse.ArgumentParser(description="Got undo tree CLI.")
    parser.add_argument(
        "init", help="Add got tracker to current directory.", action=Init
    )
    parser.add_argument(
        "-g", "--git", help="Use git on your got.", nargs=argparse.REMAINDER,
    )
    parser.parse_args()

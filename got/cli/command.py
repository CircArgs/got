import argparse
from .actions import Init


def command():
    parser = argparse.ArgumentParser(description="Got undo tree CLI.")
    parser.add_argument(
        "init", help="Add got tracker to current directory.", action=Init
    )
    parser.parse_args()

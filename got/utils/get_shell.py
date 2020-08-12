from shellingham import detect_shell, ShellDetectionFailure
from vistir.compat import Path
import os


def get_shell():
    try:
        name, path = detect_shell(os.getpid())
    except (RuntimeError, ShellDetectionFailure):
        shell = None

        if os.name == "posix":
            shell = os.environ.get("SHELL")
        elif os.name == "nt":
            shell = os.environ.get("COMSPEC")

        if not shell:
            raise RuntimeError("Unable to detect the current shell.")

        name, path = Path(shell).stem, shell
    return name, path

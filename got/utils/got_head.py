from got.macros.GIT import GIT
from ..exceptions import GotCommitException


def got_head(got_path):
    out, err = GIT("rev-parse HEAD", got_path=got_path)
    if not err.strip():
        raise GotCommitException(err)
    return out.splitlines()[0]

from got.macros.GIT import GIT


def got_head():
    out, err = GIT("rev-parse HEAD")
    return out.splitlines()[0]

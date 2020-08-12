import os
from ..exceptions import NotGotException


def is_got(path=os.getcwd()):
    potential_path = os.path.join(path, ".got")
    if os.path.exists(potential_path):
        return potential_path
    else:
        raise NotGotException(
            "This directory ({}) does not contain a got repository.".format(path)
        )

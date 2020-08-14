from random import choice
import os


class NameGenerator:
    def __init__(self):
        local = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(local, "adjectives.txt")) as f:
            self.adjectives = f.read().split("\n")
        with open(os.path.join(local, "nouns.txt")) as f:
            self.nouns = f.read().split("\n")

    def generate_name(self, attempts: int = 3):
        """
        generates whitespace free english names of adjective_noun preferring shorter names

        attempts (int): number of times to randomly create a name. shortest of n attempts returned
            will be coerced to nonnegative integer
        """
        attempts = max(abs(int(attempts)), 1)
        return sorted(
            [
                "{}_{}".format(choice(self.adjectives), choice(self.nouns))
                for i in range(attempts)
            ],
            key=len,
        )[0]

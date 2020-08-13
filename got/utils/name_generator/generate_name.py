from random import choice

with open("./adjectives.txt") as f:
    adjectives = f.readlines()
with open("./nouns.txt") as f:
    nouns = f.readlines()


def generate_name(attempts: int = 3):
    """
    generates whitespace free english names of adjective_noun preferring shorter names

    attempts (int): number of times to randomly create a name. shortest of n attempts returned
        will be coerced to nonnegative integer
    """
    attempts = max(abs(int(attempts)), 1)
    return sorted(
        ["{}_{}".format(choice(adjectives), choice(nouns)) for i in range(attempts)],
        key=len,
    )[0]

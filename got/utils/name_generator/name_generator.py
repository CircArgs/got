import os


class NameGenerator:
    def __init__(self):
        self.local = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(self.local, "determiners.txt")) as f:
            self.determiners = f.read().split("\n")

        with open(os.path.join(self.local, "plural_determiners.txt")) as f:
            self.plural_determiners = f.read().split("\n")

        with open(os.path.join(self.local, "adjectives.txt")) as f:
            self.adjectives = f.read().split("\n")

        with open(os.path.join(self.local, "nouns.txt")) as f:
            self.nouns = f.read().split("\n")

        with open(os.path.join(self.local, "adverbs.txt")) as f:
            self.adverbs = f.read().split("\n")

        with open(os.path.join(self.local, "auxiliary_verbs.txt")) as f:
            self.auxiliary_verbs = f.read().split("\n")

        with open(os.path.join(self.local, "verbs.txt")) as f:
            self.verbs = f.read().split("\n")

        self.n_determiners = len(self.determiners) + len(self.plural_determiners)
        self.n_adjectives = len(self.adjectives)
        self.n_nouns = len(self.nouns)
        self.n_adverbs = len(self.adverbs)
        self.n_aux_verbs = len(self.auxiliary_verbs)
        self.n_verbs = len(self.verbs)

    def generate_name(self, hash, n=4):
        """
        given a hash, return an english name based on the first n digits of the hash
        | 42          | 4895       | 1654  | 296     | 2         | 1042  |  |                 |                 |
        | ----------- | ---------- | ----- | ------- | --------- | ----- |  | --------------- | --------------- |
        | determiners | adjectives | nouns | adverbs | aux verbs | verbs |  | min             | max             |
        |             | x          | x     |         |           |       |  | 0               | 8096330         |
        | x           |            | x     |         |           |       |  | 8096330         | 8165798         |
        | x           |            | x     |         | x         | x     |  | 8165798         | 152937110       |
        | x           | x          | x     |         | x         | x     |  | 152937110       | 708808509350    |
        | x           | x          | x     | x       | x         | x     |  | 708808509350    | 210470857892390 |
        | x           |            | x     | x       | x         | x     |  | 210470857892390 | 210513710200742 |
        |             | x          | x     |         | x         | x     |  | 210513710200742 | 210530582952462 |
        |             | x          | x     | x       | x         | x     |  | 210530582952462 | 215524917461582 |
        hash (hexadecimal string): sha1 hash
        n (int: default 4): number of characters to use from beggining of hash (like short hash is 7 by default in git)
            try to get away with as low a number as possible for better names
        """
        # 16**11 < 210470857892390
        num = int(hash[:n], 16)

        bound = 8096330
        if num < bound:
            n_adj = num % self.n_adjectives
            n_noun = num % self.n_nouns
            return "{}_{}".format(
                self.adjectives[n_adj].replace(" ", ""),
                self.nouns[n_noun].replace(" ", ""),
            )

        bound = 8165798
        if num < bound:

            n_det = num % self.n_determiners
            n_noun = num % self.n_nouns

            det = (self.determiners + self.plural_determiners)[n_det].replace(" ", "")
            noun = self.nouns[n_noun].replace(" ", "")
            if det in self.plural_determiners:
                noun += "s"
            return "{}_{}".format(det, noun)

        bound = 152937110
        if num < bound:
            n_det = num % self.n_determiners
            n_noun = num % self.n_nouns
            n_aux = num % self.n_aux_verbs
            n_verb = num % self.n_verbs
            det = (self.determiners + self.plural_determiners)[n_det].replace(" ", "")
            noun = self.nouns[n_noun].replace(" ", "")
            if det in self.plural_determiners:
                noun += "s"
            aux = self.auxiliary_verbs[n_aux]
            verb = self.verbs[n_verb]
            return "{}_{}_{}_{}".format(det, noun, aux, verb)

        bound = 708808509350
        if num < bound:
            n_det = num % self.n_determiners
            n_adj = num % self.n_adjectives
            n_noun = num % self.n_nouns
            n_aux = num % self.n_aux_verbs
            n_verb = num % self.n_verbs
            det = (self.determiners + self.plural_determiners)[n_det].replace(" ", "")
            adj = self.adjectives[n_adj].replace(" ", "")
            noun = self.nouns[n_noun].replace(" ", "")
            if det in self.plural_determiners:
                noun += "s"
            aux = self.auxiliary_verbs[n_aux]
            verb = self.verbs[n_verb]
            return "{}_{}_{}_{}_{}".format(det, adj, noun, aux, verb)
        bound = 210470857892390
        if num < bound:
            n_adj = num % self.n_adjectives
            n_noun = num % self.n_nouns
            n_aux = num % self.n_aux_verbs
            n_verb = num % self.n_verbs

            adj = self.adjectives[n_adj].replace(" ", "")
            noun = self.nouns[n_noun].replace(" ", "")
            aux = self.auxiliary_verbs[n_aux]
            verb = self.verbs[n_verb]
            return "{}_{}_{}_{}".format(adj, noun, aux, verb)

        # wont reach this given hash[:11]
        return hash
        # currently not needed last 3 rows (they do not get us anywhere near over 16**12)
        # 210513710200742
        # 210530582952462
        # 215524917461582

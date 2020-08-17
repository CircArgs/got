class GotNode:
    def __init__(self, name, hash, info=""):

        super().__init__(tag=hash, identifier=name, data={"name": name, "info": info})

    def __repr__(self):
        return """name: {}
hash: {}
info: {}""".format(
            self.name, self.hash, self.info
        )

    @property
    def hash(self):
        return self.tag

    @property
    def name(self):
        return self.identifier

    @property
    def info(self):
        return self.data["info"]


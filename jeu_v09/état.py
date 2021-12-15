class État:
    def __init__(self):
        self.pos = 0
        self.tuiles = None


def actualiser(état):
    état.pos += 1

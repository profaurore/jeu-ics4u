class État:
    def __init__(self):
        self.pos = 0
        self.tuiles = None
        self.terrain = None


def actualiser(état):
    état.pos += 1


def charger_monde(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        données = f.read()

    print(données)

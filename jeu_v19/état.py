class État:
    def __init__(self):
        # Modes
        self.mode_débogage = False

        # Cache des images
        self.tuiles = None
        self.images = None

        # Données du jeu
        self.niveau = None
        self.ecs = None


class Niveau:
    def __init__(self):
        self.terrain = None


def actualiser(état):
    for système in état.ecs.systèmes:
        système(état)


def charger_monde(fichier):
    def analyser_terrain(lignes):
        # Retirer la balise « terrain » du début.
        lignes.pop(0)

        terrain = []
        while True:
            ligne = lignes.pop(0)
            if ligne == '/terrain':
                break

            rangée = []
            terrain.append(rangée)

            ligne = ligne.split(',')
            for tuile in ligne:
                rangée.append(int(tuile))

        terrain = [list(r) for r in zip(*terrain)]

        return terrain

    with open(fichier, 'r', encoding='utf-8') as f:
        données = f.read()

    lignes = données.splitlines()
    lignes = list(filter(len, lignes))
    lignes = list(map(str.strip, lignes))

    niveau = Niveau()

    niveau.terrain = analyser_terrain(lignes)

    return niveau

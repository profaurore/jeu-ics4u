class État:
    def __init__(self):
        self.pos = 0
        self.tuiles = None
        self.terrain = None
        self.ecs = None


def actualiser(état):
    état.pos += 1
    
    for système in état.ecs.systèmes:
        système(état)


def charger_monde(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        données = f.read()

    lignes = données.splitlines()
    lignes = list(filter(len, lignes))
    lignes = list(map(str.strip, lignes))

    terrain = []
    for ligne in lignes:
        rangée = []
        terrain.append(rangée)

        ligne = ligne.split(',')
        for tuile in ligne:
            rangée.append(int(tuile))

    terrain = [list(r) for r in zip(*terrain)]

    return terrain

import constantes as C
import pygame.freetype as freetype


class État:
    def __init__(self):
        # Modes
        self.mode_débogage = False

        # Cache des images
        self.tuiles = None
        self.images = None

        # Polices
        self.police = freetype.Font(None, 26)

        # Données du jeu
        self.niveau = None
        self.ecs = None
        self.état = C.ÉTAT_NIVEAU


class Niveau:
    def __init__(self):
        self.terrain = None
        self.l = 0
        self.h = 0
        self.joueur_init_coords = None
        self.entités_init = []


def actualiser(état):
    if état.état == C.ÉTAT_NIVEAU:
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

    def analyser_joueur(lignes):
        ligne = lignes.pop(0)
        parties = ligne.split()

        coordonnées = []
        for partie in parties[2:]:
            x, y = partie.split(',')
            coordonnées.append((int(x), int(y)))

        if parties[1] == 'rectangle':
            x1, y1 = coordonnées[0]
            x2, y2 = coordonnées[1]

            coordonnées = []
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    coordonnées.append((x, y))

        return coordonnées

    def analyser_entité(lignes):
        ligne = lignes.pop(0)
        parties = ligne.split()

        if parties[1] == 'téléportation':
            position = parties[2].split(',')
            cible = parties[3].split(',')

            entité = {
                'type': parties[1],
                'x': int(position[0]),
                'y': int(position[1]),
                'cx': int(cible[0]),
                'cy': int(cible[1])
            }
        else:
            raise ValueError(f'Entité inconnue: {parties[1]}')

        return entité

    with open(fichier, 'r', encoding='utf-8') as f:
        données = f.read()

    lignes = données.splitlines()
    lignes = list(filter(len, lignes))
    lignes = list(map(str.strip, lignes))

    niveau = Niveau()

    lignes.pop(0)
    while lignes:
        ligne = lignes[0]
        balise = ligne.split()[0]

        if balise == 'terrain':
            niveau.terrain = analyser_terrain(lignes)
            niveau.l = len(niveau.terrain)
            niveau.h = len(niveau.terrain[0])
        elif balise == 'joueur':
            niveau.joueur_init_coords = analyser_joueur(lignes)
        elif balise == 'entité':
            niveau.entités_init.append(analyser_entité(lignes))
        elif balise == '/niveau':
            lignes.pop(0)
            break
        else:
            raise ValueError(f'Balise inconnue: {balise}')

    return niveau

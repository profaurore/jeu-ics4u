import pygame
import constantes as C
from composants import *


def charger_tuiles():
    tuiles = {
        C.TUILE_T_TERRAIN: 'tuile_terrain.png',
        C.TUILE_T_MUR: 'tuile_mur.png',
        C.TUILE_T_EAU: 'tuile_eau.png',
        C.TUILE_T_FEU: 'tuile_feu.png'
    }

    for id_tuile, fichier in tuiles.items():
        tuiles[id_tuile] = pygame.image.load(C.RESSOURCES.joinpath(fichier))

    return tuiles


def rendre(ctx, état, interpolation):
    ctx.surface.fill(C.COULEUR_FOND)

    for x, rangée in enumerate(état.terrain):
        for y, tuile in enumerate(rangée):
            image = état.tuiles[tuile]

            pos = (x * C.TUILE_TAILLE, y * C.TUILE_TAILLE)

            ctx.surface.blit(image, pos)

    for d in état.ecs.composants[Débogage].values():
        pos_interpolée = int(d.x + 1 * interpolation)
        pygame.draw.rect(ctx.surface, (0, 0, 0), (pos_interpolée % (C.LARGEUR - d.taille), 0, d.taille, d.taille))

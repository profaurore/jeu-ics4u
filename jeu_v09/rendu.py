import pygame
import constantes as C


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

    terrain = [
        [0, 0, 1, 2, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    for y, rangée in enumerate(terrain):
        for x, tuile in enumerate(rangée):
            image = état.tuiles[tuile]

            pos = (x * C.TUILE_TAILLE, y * C.TUILE_TAILLE)

            ctx.surface.blit(image, pos)

    pos_interpolée = int(état.pos + 1 * interpolation)
    pygame.draw.rect(ctx.surface, (0, 0, 0), (pos_interpolée % (C.LARGEUR - 10), 0, 10, 10))

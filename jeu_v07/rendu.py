import pygame
import constantes as C


def rendre(ctx, état, interpolation):
    ctx.surface.fill(C.COULEUR_FOND)

    terrain = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    for y, rangée in enumerate(terrain):
        for x, tuile in enumerate(rangée):
            couleur = (x * 20, y * 20, 0)

            pos = (x * C.TUILE_TAILLE,
                    y * C.TUILE_TAILLE,
                    C.TUILE_TAILLE,
                    C.TUILE_TAILLE)

            pygame.draw.rect(ctx.surface, couleur, pos)

    pos_interpolée = int(état.pos + 1 * interpolation)
    pygame.draw.rect(ctx.surface, (0, 0, 0), (pos_interpolée % (C.LARGEUR - 10), 0, 10, 10))

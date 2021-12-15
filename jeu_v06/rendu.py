import pygame
import constantes as C


def rendre(ctx, état, interpolation):
    ctx.surface.fill(C.COULEUR_FOND)

    for x in range(5):
        for y in range(3):
            couleur = (x * 20, y * 20, 0)

            pos = (x * C.TUILE_TAILLE,
                    y * C.TUILE_TAILLE,
                    C.TUILE_TAILLE,
                    C.TUILE_TAILLE)

            pygame.draw.rect(ctx.surface, couleur, pos)

    pos_interpolée = int(état.pos + 1 * interpolation)
    pygame.draw.rect(ctx.surface, (0, 0, 0), (pos_interpolée % (C.LARGEUR - 10), 0, 10, 10))

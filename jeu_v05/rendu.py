import pygame
import constantes as C


def rendre(ctx, état, interpolation):
    pos_interpolée = int(état.pos + 1 * interpolation)

    ctx.surface.fill(C.COULEUR_FOND)
    pygame.draw.rect(ctx.surface, (0, 0, 0), (pos_interpolée % (C.LARGEUR - 10), 0, 10, 10))

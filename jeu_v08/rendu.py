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
            image = pygame.image.load(C.RESSOURCES.joinpath('tuile_terrain.png'))

            pos = (x * C.TUILE_TAILLE, y * C.TUILE_TAILLE)

            ctx.surface.blit(image, pos)

    pos_interpolée = int(état.pos + 1 * interpolation)
    pygame.draw.rect(ctx.surface, (0, 0, 0), (pos_interpolée % (C.LARGEUR - 10), 0, 10, 10))

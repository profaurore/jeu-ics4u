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


def charger_images():
    images = {
        'joueur': 'joueur.png'
    }

    for id_image, fichier in images.items():
        images[id_image] = pygame.image.load(C.RESSOURCES.joinpath(fichier))

    return images


def rendre(ctx, état, interpolation):
    ctx.surface.fill(C.COULEUR_FOND)

    if état.mode_débogage:
        bordure_tuile = pygame.Surface((C.TUILE_TAILLE, C.TUILE_TAILLE), pygame.SRCALPHA)
        pygame.draw.rect(bordure_tuile, C.TUILE_BORDURE, (0, 0, C.TUILE_TAILLE, C.TUILE_TAILLE), 1)

    for x, rangée in enumerate(état.niveau.terrain):
        for y, tuile in enumerate(rangée):
            image = état.tuiles[tuile]

            pos = (x * C.TUILE_TAILLE, y * C.TUILE_TAILLE)

            ctx.surface.blit(image, pos)

            if état.mode_débogage:
                ctx.surface.blit(bordure_tuile, pos)

    if état.mode_débogage:
        bordure_sprite = pygame.Surface((C.TUILE_TAILLE, C.TUILE_TAILLE), pygame.SRCALPHA)
        pygame.draw.rect(bordure_sprite, C.SPRITE_BORDURE, (0, 0, C.TUILE_TAILLE, C.TUILE_TAILLE), 1)

    for entité, sprite in état.ecs.composants[Sprite].items():
        if entité not in état.ecs.composants[Position]:
            continue
        
        position = état.ecs.composants[Position][entité]
        position_calculée = (position.x * C.TUILE_TAILLE, position.y * C.TUILE_TAILLE)

        image = état.images[sprite.image]
        ctx.surface.blit(image, position_calculée)

        if état.mode_débogage:
            ctx.surface.blit(bordure_sprite, position_calculée)

    if état.mode_débogage:
        for d in état.ecs.composants[Débogage].values():
            pos_interpolée = int(d.x + 1 * interpolation)
            pygame.draw.rect(ctx.surface, (0, 0, 0), (pos_interpolée % (C.LARGEUR - d.taille), 0, d.taille, d.taille))

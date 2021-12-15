import pygame
import constantes as C
from composants import *


def traiter(état):
    continue_jeu = True

    for événement in pygame.event.get():
        if événement.type == pygame.QUIT:
            continue_jeu = False
            break
        elif état.état == C.ÉTAT_NIVEAU:
            if événement.type == pygame.KEYDOWN:
                clé = événement.key
                if clé == pygame.K_ESCAPE:
                    continue_jeu = False
                    break
                elif clé == pygame.K_m:
                    état.mode_débogage = not état.mode_débogage
                elif clé == pygame.K_w:
                    état.ecs.composants[Force][état.joueur].direction = C.DIRECTION_N
                elif clé == pygame.K_d:
                    état.ecs.composants[Force][état.joueur].direction = C.DIRECTION_E
                elif clé == pygame.K_s:
                    état.ecs.composants[Force][état.joueur].direction = C.DIRECTION_S
                elif clé == pygame.K_a:
                    état.ecs.composants[Force][état.joueur].direction = C.DIRECTION_O
            elif événement.type == pygame.KEYUP:
                clé = événement.key
                force = état.ecs.composants[Force][état.joueur]
                direction = force.direction
                if clé == pygame.K_w and direction == C.DIRECTION_N \
                    or clé == pygame.K_a and direction == C.DIRECTION_O \
                    or clé == pygame.K_s and direction == C.DIRECTION_S \
                    or clé == pygame.K_d and direction == C.DIRECTION_E:
                    force.direction = None

    return continue_jeu

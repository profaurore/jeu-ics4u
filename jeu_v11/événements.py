import pygame


def traiter():
    continue_jeu = True

    for événement in pygame.event.get():
        if événement.type == pygame.QUIT:
            continue_jeu = False
            break
        elif événement.type == pygame.KEYDOWN:
            if événement.key == pygame.K_ESCAPE:
                continue_jeu = False
                break

    return continue_jeu

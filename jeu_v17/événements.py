import pygame


def traiter(état):
    continue_jeu = True

    for événement in pygame.event.get():
        if événement.type == pygame.QUIT:
            continue_jeu = False
            break
        elif événement.type == pygame.KEYDOWN:
            clé = événement.key
            if clé == pygame.K_ESCAPE:
                continue_jeu = False
                break
            elif clé == pygame.K_m:
                état.mode_débogage = not état.mode_débogage

    return continue_jeu

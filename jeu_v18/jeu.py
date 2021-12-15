import pygame
import constantes as C
from état import État, actualiser, charger_monde
from événements import traiter
from fenêtre import créer_fenêtre, actualiser_fenêtre
from rendu import rendre, charger_tuiles, charger_images
from ecs import ECS, ajouter_type_composant, ajouter_système
from composants import *
from entités import créer_carré_débogage, créer_joueur
from systèmes import déplacer_carré_débogage


def main():
    état = État()
    état.tuiles = charger_tuiles()
    état.images = charger_images()
    état.terrain = charger_monde(C.DÉF_MONDE_SOURCE)

    état.ecs = ECS()
    ajouter_type_composant(état.ecs, Débogage, Position, Sprite)
    ajouter_système(état.ecs, déplacer_carré_débogage)
    créer_carré_débogage(état.ecs)
    créer_joueur(état.ecs)

    ctx = créer_fenêtre()

    temps_accumulé = 0
    horloge = pygame.time.Clock()

    while True:
        horloge.tick()
        temps_écoulé = horloge.get_time()
        temps_accumulé += temps_écoulé

        if not traiter(état):
            break

        no_actualisation = 0
        while temps_accumulé >= C.DT and no_actualisation < 3:
            actualiser(état)
            temps_accumulé -= C.DT
            no_actualisation += 1

        interpolation = temps_accumulé / C.DT
        rendre(ctx, état, interpolation)
        actualiser_fenêtre(ctx)


main()

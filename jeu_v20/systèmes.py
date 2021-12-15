import constantes as C
from composants import *


def déplacer_carré_débogage(état):
    if not état.mode_débogage:
        return

    débogages = état.ecs.composants[Débogage]
    for débogage in débogages.values():
        débogage.x = (débogage.x + 1) % (C.LARGEUR - débogage.taille)


def appliquer_forces(état):
    def calculer_cible(position, direction):
        x = position.x
        y = position.y

        if direction == C.DIRECTION_N:
            y -= 1
        elif direction == C.DIRECTION_E:
            x += 1
        elif direction == C.DIRECTION_S:
            y += 1
        elif direction == C.DIRECTION_O:
            x -= 1

        return x, y

    for entité, force in état.ecs.composants[Force].items():
        # Passer à la prochaine si l'entité n'a pas de force ou n'a pas une position.
        if force.direction is None or entité not in état.ecs.composants[Position]:
            continue

        position = état.ecs.composants[Position][entité]

        cible = calculer_cible(position, force.direction)
        position.x, position.y = cible

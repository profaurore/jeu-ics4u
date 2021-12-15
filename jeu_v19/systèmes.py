import constantes as C
from composants import *


def déplacer_carré_débogage(état):
    if not état.mode_débogage:
        return

    débogages = état.ecs.composants[Débogage]
    for débogage in débogages.values():
        débogage.x = (débogage.x + 1) % (C.LARGEUR - débogage.taille)

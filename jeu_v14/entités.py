from composants import *
from ecs import créer_entité, ajouter_composant


def créer_carré_débogage(ecs):
    carré = créer_entité(ecs)
    ajouter_composant(ecs, carré, Débogage())
    return carré

from composants import *
from ecs import créer_entité, ajouter_composant
import constantes as C


def créer_carré_débogage(ecs):
    carré = créer_entité(ecs)
    ajouter_composant(ecs, carré,
        Débogage()
    )
    return carré


def créer_joueur(ecs):
    joueur = créer_entité(ecs)
    ajouter_composant(ecs, joueur,
        Joueur(),
        Position(),
        Sprite('joueur'),
        Force(),
        MouvementGrillage(5)
    )
    return joueur


def créer_téléportation(ecs, x, y, cx, cy):
    téléportation = créer_entité(ecs)
    ajouter_composant(ecs, téléportation,
        Position(x, y),
        Téléportation(cx, cy)
    )
    return téléportation

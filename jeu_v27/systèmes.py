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
        x = int(position.x)
        y = int(position.y)

        if direction == C.DIRECTION_N:
            y -= 1
        elif direction == C.DIRECTION_E:
            x += 1
        elif direction == C.DIRECTION_S:
            y += 1
        elif direction == C.DIRECTION_O:
            x -= 1

        if 0 <= x < état.niveau.l and 0 <= y < état.niveau.h:
            return x, y

        return None

    def peut_entrer_tuile(entité, tuile):
        if tuile in [C.TUILE_T_MUR]:
            return False

        return True

    for entité, force in état.ecs.composants[Force].items():
        # Passer à la prochaine si l'entité n'a pas de force ou n'a pas une position.
        if force.direction is None or entité not in état.ecs.composants[Position]:
            continue

        position = état.ecs.composants[Position][entité]

        cible = calculer_cible(position, force.direction)
        if cible:
            tuile = état.niveau.terrain[cible[0]][cible[1]]
            if peut_entrer_tuile(entité, tuile):
                if entité in état.ecs.composants[MouvementGrillage]:
                    mouvement = état.ecs.composants[MouvementGrillage][entité]
                    if mouvement.restant is None:
                        mouvement.restant = mouvement.durée
                        mouvement.sx = position.x
                        mouvement.sy = position.y
                        mouvement.cx, mouvement.cy = cible
                else:
                    position.x, position.y = cible
                    arriver_centre_tuile(état, entité, cible[0], cible[1])


def appliquer_mouvement_grillage(état):
    for entité, mouvement in état.ecs.composants[MouvementGrillage].items():
        if mouvement.restant is None:
            continue

        mouvement.restant -= 1
        if mouvement.restant == 0:
            est_déplacement = False
            if entité in état.ecs.composants[Position]:
                est_déplacement = mouvement.sx != mouvement.cx or mouvement.sy != mouvement.cy

                position = état.ecs.composants[Position][entité]
                position.x = mouvement.cx
                position.y = mouvement.cy

            mouvement.restant = mouvement.sx = mouvement.sy = mouvement.cx = mouvement.cy = None
            
            if est_déplacement:
                arriver_centre_tuile(état, entité, position.x, position.y)
        elif entité in état.ecs.composants[Position]:
            position = état.ecs.composants[Position][entité]

            interp_mvt = 1 - mouvement.restant / mouvement.durée
            position.x = mouvement.sx * (1 - interp_mvt) + mouvement.cx * interp_mvt
            position.y = mouvement.sy * (1 - interp_mvt) + mouvement.cy * interp_mvt


def arriver_centre_tuile(état, entité, x, y):
    tuile = état.niveau.terrain[x][y]
    if tuile == C.TUILE_T_EAU:
        if entité in état.ecs.composants[Position] and entité in état.ecs.composants[MouvementGrillage]:
            position = état.ecs.composants[Position][entité]
            mouvement = état.ecs.composants[MouvementGrillage][entité]

            mouvement.restant = mouvement.durée
            mouvement.sx = mouvement.cx = position.x
            mouvement.sy = mouvement.cy = position.y
    elif tuile == C.TUILE_T_FEU:
        if entité in état.ecs.composants[Joueur]:
            état.état = C.ÉTAT_ÉCHEC

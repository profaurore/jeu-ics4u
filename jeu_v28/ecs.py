class ECS:
    def __init__(self):
        self.dernière_entité = 0
        self.composants = {}
        self.systèmes = []
        self.entités = set()


def créer_entité(ecs):
    ecs.dernière_entité += 1
    ecs.entités.add(ecs.dernière_entité)
    return ecs.dernière_entité


def supprimer_entité(ecs, entité):
    for composants in ecs.composants.items():
        if entité in composants:
            del composants[entité]
    ecs.entités.remove(entité)


def ajouter_type_composant(ecs, *types_composants):
    for t in types_composants:
        ecs.composants[t] = {}


def supprimer_type_composant(ecs, *types_composants):
    for t in types_composants:
        del ecs.composants[t]


def ajouter_système(ecs, *systèmes):
    for s in systèmes:
        ecs.systèmes.append(s)


def supprimer_système(ecs, *systèmes):
    for s in systèmes:
        ecs.systèmes.remove(s)


def ajouter_composant(ecs, entité, *composants):
    for c in composants:
        ecs.composants[c.__class__][entité] = c


def supprimer_composant(ecs, entité, *composants):
    for c in composants:
        del ecs.composants[c.__class__][entité]

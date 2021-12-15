import pygame
import ctypes

# Titre qui sera affiché dans la barre de titre
TITRE = 'Mon jeu'

# Largeur du contenu de la fenêtre
LARGEUR = 640

# Hauteur du contenu de la fenêtre
HAUTEUR = 480

# Indique si le mode d'écran à haut DPI doit être activé
HAUT_DPI = True

# Couleur d'arrière plan
COULEUR_FOND = (255, 255, 255)

# Millisecondes entre chaque actualisation
DT = 50


class État:
    def __init__(self):
        self.pos = 0


class ContexteGraphique:
    def __init__(self):
        self.fenêtre = None
        self.surface = None


def initialiser_système_graphique():
    # Initialise PyGame.
    pygame.init()

    # Paramétrer les écrans à haut DPI.
    if HAUT_DPI:
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()


def créer_fenêtre():
    ctx = ContexteGraphique()

    # Crée une fenêtre et obtenir la surface de dessin.
    ctx.fenêtre = pygame.display.set_mode((LARGEUR, HAUTEUR))
    ctx.surface = pygame.Surface(ctx.fenêtre.get_size(), pygame.SRCALPHA | pygame.HWSURFACE)

    # Défini le texte de la barre de titre.
    pygame.display.set_caption(TITRE)

    return ctx


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


def actualiser(état):
    état.pos += 1


def rendre(ctx, état, interpolation):
    pos_interpolée = int(état.pos + 1 * interpolation)

    ctx.surface.fill(COULEUR_FOND)
    pygame.draw.rect(ctx.surface, (0, 0, 0), (pos_interpolée % (LARGEUR - 10), 0, 10, 10))

    actualiser_fenêtre(ctx)


def actualiser_fenêtre(ctx):
    # Dessine le dessin dans la fenêtre.
    ctx.fenêtre.blit(ctx.surface, (0, 0))

    # Mets à jour la fenêtre.
    pygame.display.flip()


def main():
    état = État()

    initialiser_système_graphique()
    ctx = créer_fenêtre()

    temps_accumulé = 0
    horloge = pygame.time.Clock()

    while True:
        horloge.tick()
        temps_écoulé = horloge.get_time()
        temps_accumulé += temps_écoulé

        if not traiter():
            break

        no_actualisation = 0
        while temps_accumulé >= DT and no_actualisation < 3:
            actualiser(état)
            temps_accumulé -= DT
            no_actualisation += 1

        interpolation = temps_accumulé / DT
        rendre(ctx, état, interpolation)


main()

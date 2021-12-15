import pygame
import ctypes
import constantes as C


class ContexteGraphique:
    def __init__(self):
        self.fenêtre = None
        self.surface = None


def initialiser_système_graphique():
    # Initialise PyGame.
    pygame.init()

    # Paramétrer les écrans à haut DPI.
    if C.HAUT_DPI:
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()


def créer_fenêtre():
    initialiser_système_graphique()

    ctx = ContexteGraphique()

    # Crée une fenêtre et obtenir la surface de dessin.
    ctx.fenêtre = pygame.display.set_mode((C.LARGEUR, C.HAUTEUR))
    ctx.surface = pygame.Surface(ctx.fenêtre.get_size(), pygame.SRCALPHA | pygame.HWSURFACE)

    # Défini le texte de la barre de titre.
    pygame.display.set_caption(C.TITRE)

    return ctx


def actualiser_fenêtre(ctx):
    # Dessine le dessin dans la fenêtre.
    ctx.fenêtre.blit(ctx.surface, (0, 0))

    # Mets à jour la fenêtre.
    pygame.display.flip()

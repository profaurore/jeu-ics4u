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


def initialiser_système_graphique():
    # Initialise PyGame.
    pygame.init()

    # Paramétrer les écrans à haut DPI.
    if HAUT_DPI:
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()


def créer_fenêtre():
    # Crée une fenêtre et obtenir la surface de dessin.
    fenêtre = pygame.display.set_mode((LARGEUR, HAUTEUR))
    surface = pygame.Surface(fenêtre.get_size(), pygame.SRCALPHA | pygame.HWSURFACE)

    # Défini le texte de la barre de titre.
    pygame.display.set_caption(TITRE)

    return fenêtre, surface


def traiter():
    pass


# NE JAMAIS FAIRE CECI EN PRATIQUE. ON VERRA DE MEILLEURS TECHNIQUES DANS QUELQUES JOURS.
pos = 0
def actualiser():
    global pos

    pos += 1


def rendre(fenêtre, surface):
    # NE JAMAIS FAIRE CECI EN PRATIQUE. ON VERRA DE MEILLEURS TECHNIQUES DANS QUELQUES JOURS.
    global pos

    surface.fill(COULEUR_FOND)
    pygame.draw.rect(surface, (0, 0, 0), (pos % (LARGEUR - 10), 0, 10, 10))

    actualiser_fenêtre(fenêtre, surface)


def actualiser_fenêtre(fenêtre, surface):
    # Dessine le dessin dans la fenêtre.
    fenêtre.blit(surface, (0, 0))

    # Mets à jour la fenêtre.
    pygame.display.flip()


def main():
    initialiser_système_graphique()
    fenêtre, surface = créer_fenêtre()

    while True:
        traiter()
        actualiser()
        rendre(fenêtre, surface)


main()

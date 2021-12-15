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
DESSIN_FOND = (255, 255, 255)


def initialise_système_graphique():
    # Initialise PyGame.
    pygame.init()

    # Paramétrer les écrans à haut DPI.
    if HAUT_DPI:
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()


def crée_fenêtre():
    # Crée une fenêtre de taille donnée.
    fenêtre = pygame.display.set_mode((LARGEUR, HAUTEUR))

    # Crée une surface où il faudra dessiner le jeu.
    surface = pygame.Surface(fenêtre.get_size(), pygame.SRCALPHA | pygame.HWSURFACE)

    # Défini le texte de la barre de titre.
    pygame.display.set_caption(TITRE)

    # Renvoie la fenêtre et la surface.
    return fenêtre, surface


def rend(fenêtre, surface):
    # Remplie la surface avec la couleur d'arrière plan.
    surface.fill(DESSIN_FOND)

    # Dessine le cheveux vertical.
    # (couleur RVB, (x1, y1), (x2, y2), largeur)
    pygame.draw.line(surface, (0, 0, 0), (320, 240), (320, 80), 4)

    # Dessine les deux cheveux diagonals.
    # (couleur RVB, lié dernier et premier points, liste de points, largeur)
    pygame.draw.lines(surface, (0, 0, 0), False, [(200, 120), (320, 240), (440, 120)], 2)

    # Dessine les oreilles.
    # (couleur, (x1, y1, x2, y2)): remplir
    pygame.draw.ellipse(surface, (255, 128, 0), (180, 200, 280, 40))
    # (couleur, (x1, y1, x2, y2), largeur): contour
    pygame.draw.ellipse(surface, (175, 110, 0), (180, 200, 280, 40), 2)

    # Dessine le visage.
    # (couleur, point centre, rayon): remplir
    pygame.draw.circle(surface, (255, 255, 0), (320, 240), 120)
    # (couleur, point centre, rayon, largeur): contour
    pygame.draw.circle(surface, (200, 200, 0), (320, 240), 120, 4)

    # Dessine les yeux.
    # (couleur, (x1, y1, x2, y2))
    pygame.draw.rect(surface, (0, 0, 0), (350, 200, 10, 10))
    pygame.draw.rect(surface, (0, 0, 0), (280, 200, 10, 10))

    # Dessine la bouche.
    # (couleur, (x1, y1, x2, y2), angle départ [en radians], angle fin [en radians])
    pygame.draw.arc(surface, (200, 0, 0), (260, 260, 120, 24), 7 * 3.14159 / 6, 11 * 3.14159 / 6)

    actualise_fenêtre(fenêtre, surface)


def actualise_fenêtre(fenêtre, surface):
    # Dessine le dessin dans la fenêtre.
    fenêtre.blit(surface, (0, 0))

    # Mets à jour la fenêtre.
    pygame.display.flip()


def main():
    initialise_système_graphique()

    fenêtre, surface = crée_fenêtre()

    rend(fenêtre, surface)

    # Arrêter le programme pendant 5 secondes.
    pygame.time.wait(5000)


main()

from pathlib import Path

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

# Taille des tuiles
TUILE_TAILLE = 40

# Ressources du jeu
RESSOURCES = Path(__file__).resolve().parent.joinpath('ressources')

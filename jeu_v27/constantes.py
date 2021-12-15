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

# Couleur de la bordure des tuiles pour le débogage.
TUILE_BORDURE = (255, 255, 255, 100)

# Couleur de la bordure des sprites pour le débogage.
SPRITE_BORDURE = (255, 0, 0, 100)

# Ressources du jeu
RESSOURCES = Path(__file__).resolve().parent.joinpath('ressources')

# Tuiles
TUILE_T_TERRAIN = 0
TUILE_T_MUR = 1
TUILE_T_EAU = 2
TUILE_T_FEU = 3

# Fichier qui défini le monde
DÉF_MONDE_SOURCE = RESSOURCES.joinpath('monde.def')

# Directions cardinales
DIRECTION_N = 1
DIRECTION_E = 2
DIRECTION_S = 3
DIRECTION_O = 4

# État du jeu
ÉTAT_NIVEAU = 0
ÉTAT_ÉCHEC = 1

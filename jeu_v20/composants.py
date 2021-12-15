class Débogage:
    def __init__(self):
        self.x = 0
        self.taille = 10


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Sprite:
    def __init__(self, image):
        self.image = image


class Force:
    def __init__(self, direction=0):
        self.direction = direction
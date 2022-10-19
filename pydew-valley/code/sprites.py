import pygame
from settings import *

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS["main"]):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z
class Water(Generic):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)

class Trees:
    pass
class WildFlowers:
    pass
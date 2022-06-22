from os import environ
import pygame
from settings import *

class BG(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("Coding/pygame-dev/graphics/environment/background.png").convert()
        self.rect = self.image.get_rect(top_left = (0, 0))
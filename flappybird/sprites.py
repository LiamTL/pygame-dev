import pygame
from settings import *

class BG(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        bg_image = pygame.image.load("C:/Users/tayel/Documents/Coding/pygame-dev/flappybird/graphics/environment/background.png").convert()

        full_width = bg_image.get_width() * scale_factor
        full_height = bg_image.get_height() * scale_factor
        full_sized_image = pygame.transform.scale(bg_image, (full_width, full_height))

        self.image = pygame.Surface((full_width * 2 ,full_height))
        self.image.blit(full_sized_image, (0,0))
        self.image.blit(full_sized_image, (full_width, 0))

        self.rect = self.image.get_rect(topleft = (0, 0))
        self.pos = pygame.math.Vector2(self.rect.topleft)


    def update(self, dt):
        self.pos.x -= 300 * dt
        if self.rect.centerx <= 0:
            self.pos.x = 0
        self.rect.x = round(self.pos.x)
class Ground(pygame.sprite.Sprite):

    def __init__(self, groups, scale_factor):
        super().__init__(groups)

        # Image
        ground_surf = pygame.image.load("../pygame-dev/flappybird/graphics/environment/ground.png").convert_alpha()
        self.image = pygame.transform.scale(ground_surf, pygame.math.Vector2(ground_surf.get_size()) * scale_factor)

        # Position
        self.rect = self.image.get_rect(bottomleft = (0,WINDOW_HEIGHT))
        self.pos = pygame.math.Vector2(self.rect.topleft)
    def update(self, dt):
        self.pos.x -= 360 * dt
        if self.rect.centerx <= 0:
            self.pos.x = 0

        self.rect.x = round(self.pos.x)

class Plane(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)

        # Image
        self.import_frames(scale_factor)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

        # Rect.
        self.rect = self.image.get_rect(midleft = (WINDOW_WIDTH / 20, WINDOW_HEIGHT / 2))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        # Movement
        self.gravity = 600
        self.direction = 0

    def import_frames(self, scale_factor):
        self.frames = []
        for i in range(3):
            surf = pygame.image.load(f'C:/Users/tayel/Documents/Coding/pygame-dev/flappybird/graphics/plane/red{i}.png').convert_alpha()
            scaled_surf = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)
            self.frames.append(scaled_surf)

    def apply_gravity(self, dt):
        self.direction += self.gravity * dt
        self.pos.y += self.direction * dt
        self.rect.y = round(self.pos.y)

    def jump(self):
        self.direction = -400

    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
    
    def rotate(self):
        rotated_plane = pygame.transform.rotozoom(self.image, -self.direction * 0.06, 1)
        self.image = rotated_plane

    def update(self, dt):
        self.apply_gravity(dt)
        self.animate(dt)
        self.rotate()
import pygame

class Tower():
    def __init__(self):
        self.levels = pygame.sprite.Group()

    def draw(self, surface):
        self.levels.draw(surface)

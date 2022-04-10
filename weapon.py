import pygame
import color

class RifleMan(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        self.direction = direction

        self.range = 150
        self.damage = 5
        self.cooldown = 50

        self.image = pygame.Surface([30, 30])
        self.image.fill(color.white)

        self.rect = (self.x, self.y)

    def update(self):
        self.rect = (self.x, self.y)
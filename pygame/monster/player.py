from pygame.sprite import Sprite
import pygame
from config import *


class Player(Sprite):
    def __init__(self):
        self.image = pygame.image.load("monster/assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = WINDOW_HEIGHT
        self.rect.centerx = WINDOW_WIDTH/2
        self.velocity = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity

    def draw(self, display_surface):
        display_surface.blit(self.image, self.rect)

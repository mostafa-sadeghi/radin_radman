import pygame
from random import randint
pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
score = 0
main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

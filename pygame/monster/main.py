import pygame
from config import *
from player import Player
pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dragon Game")


my_player = Player()

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    my_player.draw(display_surface)
    my_player.update()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

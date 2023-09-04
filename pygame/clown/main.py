import pygame
from random import randint, choice
pygame.init()
WINDOW_WIDTH = 967
WINDOW_HEIGHT = 655
score = 0
main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

bg_pic = pygame.image.load("background.png")
bg_pic_rect = bg_pic.get_rect()
bg_pic_rect.topleft = (0, 0)
clown = pygame.image.load("clown.png")
clown_rect = clown.get_rect()
clown_rect.topleft = (WINDOW_WIDTH/2-50, WINDOW_HEIGHT/2)

FPS = 60
dx = choice([-1, 1])
dy = choice([-1, 1])
clown_velocity = 5
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clown_rect.x += dx * clown_velocity
    clown_rect.y += dy * clown_velocity

    if clown_rect.left <= 0 or clown_rect.right >= WINDOW_WIDTH:
        dx *= -1
    if clown_rect.top <= 0 or clown_rect.bottom >= WINDOW_HEIGHT:
        dy *= -1

    main_surface.blit(bg_pic, bg_pic_rect)
    main_surface.blit(clown, clown_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

import pygame

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
FPS = 60
clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
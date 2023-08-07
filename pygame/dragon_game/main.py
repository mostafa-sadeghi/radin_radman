import pygame

pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dragon Game")

font = pygame.font.Font("minecraft.ttf", 22)
title_text = font.render("Dragon Game", True, (0, 255, 0))
# TODO   قرادادن متن در بالای صفحه

" قرار دادن بازکین دراگون در وسط سمت چپ صفحع"


dragon_left = pygame.image.load("dragon.png")
dragon_left_rect = dragon_left.get_rect()
dragon_left_rect.topleft = (0,0)

dragon_right = pygame.transform.flip(dragon_left, True, False)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


    main_surface.blit(dragon_left, dragon_left_rect)
    main_surface.blit(dragon_right, (WINDOW_WIDTH-48,0))
    pygame.display.update()

pygame.quit()

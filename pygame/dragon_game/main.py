import pygame

pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dragon Game")

font = pygame.font.Font("dragon_game\\minecraft.ttf",
                        62)
title_text = font.render("Dragon Game", True,
                         (0, 255, 0))
title_rect = title_text.get_rect()
title_rect.top = 0
title_rect.centerx = WINDOW_WIDTH/2

dragon_left = pygame.image.load("dragon_game\\dragon.png")
dragon_left_rect = dragon_left.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right = pygame.transform.flip(dragon_left, True, False)

player_image = dragon_right
player_rect = player_image.get_rect()
player_rect.left = 40
player_rect.centery = WINDOW_HEIGHT/2 + 20
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 50:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    main_surface.fill((0,0,0))
    main_surface.blit(dragon_left, dragon_left_rect)
    main_surface.blit(dragon_right, (WINDOW_WIDTH-48, 0))
    main_surface.blit(title_text, title_rect)
    pygame.draw.line(main_surface,
                     (0, 255, 0), (0, 50),
                     (WINDOW_WIDTH, 50), 4)
    
    main_surface.blit(player_image, player_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

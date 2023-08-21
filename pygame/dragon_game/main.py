import pygame
from random import randint
pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dragon Game")

font = pygame.font.Font("minecraft.ttf",
                        62)
title_text = font.render("Dragon Game", True,
                         (0, 255, 0))
title_rect = title_text.get_rect()
title_rect.top = 0
title_rect.centerx = WINDOW_WIDTH/2

dragon_left = pygame.image.load("dragon.png")
dragon_left_rect = dragon_left.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right = pygame.transform.flip(dragon_left, True, False)

player_image = dragon_right
player_rect = player_image.get_rect()
player_rect.left = 40
player_rect.centery = WINDOW_HEIGHT/2 + 20


food = pygame.image.load("food.png")
food_rect = food.get_rect()
food_rect.center = (WINDOW_WIDTH + 100 , randint(80, WINDOW_HEIGHT - 80))


pygame.mixer.music.load("bg.mp3")
pygame.mixer.music.play(-1)

lose_sound = pygame.mixer.Sound("lose.wav")
lose_sound.set_volume(0.3)

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
    if keys[pygame.K_DOWN] and player_rect.bottom <= WINDOW_HEIGHT:
        player_rect.y += 5
    

    food_rect.x -= 5
    if food_rect.x <= 0:
        food_rect.center = (WINDOW_WIDTH + 100 , randint(80, WINDOW_HEIGHT - 80))
        lose_sound.play()



    main_surface.fill((0,0,0))
    main_surface.blit(dragon_left, dragon_left_rect)
    main_surface.blit(dragon_right, (WINDOW_WIDTH-48, 0))
    main_surface.blit(title_text, title_rect)
    pygame.draw.line(main_surface,
                     (0, 255, 0), (0, 50),
                     (WINDOW_WIDTH, 50), 4)
    
    main_surface.blit(player_image, player_rect)
    main_surface.blit(food, food_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

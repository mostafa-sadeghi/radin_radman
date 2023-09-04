import pygame

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
FPS = 60
STARTING_BOOST_LEVEL = 100

boost_level = STARTING_BOOST_LEVEL

clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

dog_original = pygame.image.load("dog/assets/dog.png")

dog_left = dog_original
dog_right = pygame.transform.flip(dog_original, True, False)

dog = dog_right
dog_rect = dog.get_rect(topleft=(WINDOW_WIDTH/2 - 32, WINDOW_HEIGHT - 64))

dog_normal_velocity = 5
dog_fast_velocity = 10
dog_velocity = dog_normal_velocity
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and dog_rect.bottom < WINDOW_HEIGHT:
        dog_rect.y += dog_velocity
    if keys[pygame.K_UP] and dog_rect.top > 100:
        dog_rect.y -= dog_velocity
    if keys[pygame.K_LEFT] and dog_rect.left > 0:
        dog = dog_left
        dog_rect.x -= dog_velocity
    if keys[pygame.K_RIGHT] and dog_rect.right < WINDOW_WIDTH:
        dog = dog_right
        dog_rect.x += dog_velocity

    if keys[pygame.K_SPACE] and boost_level > 0:
        boost_level -= 1
        dog_velocity = dog_fast_velocity
    else:
        dog_velocity = dog_normal_velocity
    
    display_surface.fill((0,0,0))
    display_surface.blit(dog, dog_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

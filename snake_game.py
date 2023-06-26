from snake_game_utils import *
from time import sleep


def on_close():
    global running
    running = False


def go_up():
    snake_head.direction = "up"


main_surface = make_screen("blue", "snake game", 600, 600)
main_surface.tracer(False)

root = main_surface._root
root.protocol('WM_DELETE_WINDOW', on_close)

snake_head = make_turtle("square", "black")
snake_head.direction = ""

snake_food = make_turtle("circle", "red")
change_food_position(snake_food)

main_surface.listen()
main_surface.onkeypress(go_up, "w")
# TODO  برای سایر جهت ها
running = True
while running:
    main_surface.update()
    move_snake(snake_head)
    sleep(0.2)

from snake_game_utils import *
from time import sleep

score = 0

def on_close():
    global running
    running = False


def go_up():
    snake_head.direction = "up"


def go_down():
    snake_head.direction = "down"


def go_left():
    snake_head.direction = "left"


def go_right():
    snake_head.direction = "right"


main_surface = make_screen("blue", "snake game", 600, 600)
main_surface.tracer(False)

root = main_surface._root
root.protocol('WM_DELETE_WINDOW', on_close)

snake_head = make_turtle("square", "black")
snake_head.direction = ""

snake_food = make_turtle("circle", "red")
change_food_position(snake_food)

score_board = make_turtle("square", "white")
score_board.ht()
score_board.goto(0,260)



main_surface.listen()
main_surface.onkeypress(go_up, "Up")
main_surface.onkeypress(go_down, "Down")
main_surface.onkeypress(go_left, "Left")
main_surface.onkeypress(go_right, "Right")
main_surface.onkeypress(go_up, "w")
main_surface.onkeypress(go_down, "s")
main_surface.onkeypress(go_left, "a")
main_surface.onkeypress(go_right, "d")
running = True
while running:
    score_board.clear()
    score_board.write(f"Score : {score}",align="center",\
                       font=("Terminal", 22, "normal"))
    main_surface.update()
    if snake_head.distance(snake_food) < 20:
        change_food_position(snake_food)
        score += 1


    move_snake(snake_head)
    sleep(0.2)

from snake_game_utils import *
from time import sleep

score = 0
high_score = 0


def on_close():
    global running
    running = False


def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def go_right():
    if snake_head.direction != "left":
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
score_board.goto(0, 260)

main_surface.listen()
main_surface.onkeypress(go_up, "Up")
main_surface.onkeypress(go_down, "Down")
main_surface.onkeypress(go_left, "Left")
main_surface.onkeypress(go_right, "Right")
main_surface.onkeypress(go_up, "w")
main_surface.onkeypress(go_down, "s")
main_surface.onkeypress(go_left, "a")
main_surface.onkeypress(go_right, "d")
snake_tails = []
running = True
while running:
    score_board.clear()
    score_board.write(f"Score : {score}\tHighScore: {high_score}", align="center", \
                      font=("Terminal", 22, "normal"))
    main_surface.update()
    if snake_head.distance(snake_food) < 20:
        change_food_position(snake_food)
        score += 1
        new_tail = make_turtle("square", "grey")
        snake_tails.append(new_tail)

    for i in range(len(snake_tails) - 1, 0, -1):
        prev_x = snake_tails[i - 1].xcor()
        prev_y = snake_tails[i - 1].ycor()
        snake_tails[i].setpos(prev_x, prev_y)
    if len(snake_tails) > 0:
        xpos_of_snake_head = snake_head.xcor()
        ypos_of_snake_head = snake_head.ycor()
        snake_tails[0].setpos(xpos_of_snake_head, ypos_of_snake_head)

    if score > high_score:
        high_score = score

    if snake_head.xcor() > 290 or \
            snake_head.xcor() < -290 \
            or snake_head.ycor() > 290 or \
            snake_head.ycor() < -290:
        reset(snake_head, snake_tails)
        score = 0

    move_snake(snake_head)
    for body in snake_tails:
        if body.distance(snake_head) < 20:
            reset(snake_head, snake_tails)
            score = 0

    sleep(0.2)


"""
    try:                                  
...     f = open("snake_scores.txt")
...     f.read()
... except:                          
...     f = open("snake_scores.txt", "w")
...     f.write("123")


"""
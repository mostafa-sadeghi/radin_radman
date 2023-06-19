from turtle import Screen
from snake_game_utils import *

def on_close():
    global running
    running = False

main_surface = Screen()
main_surface.bgcolor('blue')
main_surface.setup(width=600, height=600)
main_surface.title("Snake Game")
main_surface.tracer(False)

root = main_surface._root
root.protocol('WM_DELETE_WINDOW', on_close)

snake_head = make_turtle("square", "black")
snake_head.goto(100,100)

running = True
while running:
    main_surface.update()

import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 8
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
turtle.hideturtle()
snake = turtle.clone()
snake.shape("square")
turtle.hideturtle()
pos = snake.pos()
for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto(my_pos[0],my_pos[1])
    stamp_list.append(my_pos)
    stamp = snake.stamp()
    stamp_list.append(stamp)




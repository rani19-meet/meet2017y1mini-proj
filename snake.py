import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)
turtle.bgcolor("blue")


turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
turtle.hideturtle()
snake = turtle.clone()
snake.shape("circle")
turtle.hideturtle()
pos = snake.pos()
for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto(my_pos[0],my_pos[1])
    stamp = snake.stamp()
    stamp_list.append(stamp)
    pos_list.append(my_pos)
print('first pos_list', pos_list)
UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW= "Right"
TIME_STEP = 300
SPACEBAR = "space"
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = UP
TOP_EDGE = SIZE_Y/2
BOTTOM_EDGE = SIZE_Y/-2
RIGHT_EDGE = SIZE_X/2
LEFT_EDGE = SIZE_X/-2

border = turtle.clone()
border.hideturtle()
border.penup()
border.goto(LEFT_EDGE, BOTTOM_EDGE)
border.pendown()
border.goto(RIGHT_EDGE, BOTTOM_EDGE)
border.goto(RIGHT_EDGE, TOP_EDGE)
border.goto(LEFT_EDGE, TOP_EDGE)
border.pendown()

border.goto(LEFT_EDGE, BOTTOM_EDGE)

turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")


def up():
    global direction
    direction=UP
    print("You pressed the up key!")

def down():
    global direction
    direction=DOWN
    print("You pressed the down key!")

def left():
    global direction
    direction=LEFT
    print("You pressed the left key!")

def right():
    global direction
    direction=RIGHT
    print("You pressed the right key!")
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.listen()
def make_food():
    
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    
    food.goto(food_x, food_y)
    random_pos = (food_x, food_y)
    food_pos.append(random_pos)
    stamp_id=food.stamp()
    food_stamps.append(stamp_id)
    
def move_snake():
    global food_stamps, food_pos
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("You have eaten the food!")
        make_food()
    else:
        # removes the tail
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    print(food_pos)
    if direction==RIGHT:
      snake.goto(x_pos + SQUARE_SIZE, y_pos)
      print("You moved right!")
    elif direction==LEFT:
      snake.goto(x_pos - SQUARE_SIZE, y_pos)
      print("You moved left!")
    elif direction==UP:
      snake.goto(x_pos, SQUARE_SIZE + y_pos)
      print("You moved up!")
    elif direction==DOWN:
      snake.goto(x_pos, y_pos - SQUARE_SIZE)
      print("You moved down!")

    # makes a new head
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! GAME OVER!")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! GAME OVER!")
        quit()
    if new_y_pos >= TOP_EDGE:
        print("You hit the top edge! GAME OVER!")
        quit()
    if new_y_pos <= BOTTOM_EDGE:
        print("You hit the bottom edge! GAME OVER!")
        quit()


    if snake.pos() in pos_list[0:-1]:
        print(snake.pos())
        print(pos_list)
        print("GAME OVER!")
        quit()

    turtle.ontimer(move_snake,TIME_STEP)
    
    
for pos_tuple in food_pos:
    food.goto(pos_tuple[0], pos_tuple[1])
    food_id = food.stamp()
    food_stamps.append(food_id)




    
    
    
    

    
make_food()
move_snake()


    
    

    
          
          
        



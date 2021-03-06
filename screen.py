
from pickle import GLOBAL
from time import sleep
import turtle, tkinter, math, random
from tkinter import messagebox


# Screen Dimensions and Delay (ms)
BORDER = 0
WIDTH, HEIGHT, DELAY, FOOD_SIZE, SCORE = 600 + BORDER, 600 + BORDER, 200, 10, 0

def reset():
    global SCORE, snake, snake_direction, food_pos, DELAY
    
    # Initial Snake on x-axis, it's direction and user score
    SCORE, DELAY, snake_direction = 0, 200, "up"
    snake = [[0,0], [20,0]]
    canvas.title('Snake')
    food_pos = generate_food_location()
    food.goto(food_pos) 
    game_loop()
    
offsets = {
    "up": (0,20),
    "down": (0,-20),
    "left": (-20,0),
    "right": (20,0)
}

# Game speed increases as snake grows
def levels():
    global DELAY
    DELAY-=10

    if DELAY <= 50:
        my_turtle.shape("circle")
    elif DELAY <= 100:
        my_turtle.color("white", "red")
    elif DELAY <= 150:
        my_turtle.color("black", "yellow")


def direction_keys():
    canvas.onkey(lambda: set_snake_direction("up"), "Up")
    canvas.onkey(lambda: set_snake_direction("down"), "Down")
    canvas.onkey(lambda: set_snake_direction("left"), "Left")
    canvas.onkey(lambda: set_snake_direction("right"), "Right")

def set_snake_direction(direction):
    '''Setting Snake Directions, snake can only make 
    90 degree turns since it shoul'd travel over itself'''

    #Global since we're updating an external variable
    global snake_direction 

    if direction == 'up':
        if snake_direction != 'down':
            snake_direction = 'up'

    elif direction == 'down':
        if snake_direction != 'up':
            snake_direction = 'down'

    elif direction == 'left':
        if snake_direction != 'right':
            snake_direction = 'left'

    elif direction == 'right':
        if snake_direction != 'left':
            snake_direction = 'right'

def game_loop():

    # Increment Head location and Pop tail location to maintain Snake Size
    my_turtle.clearstamps()
    new_head = snake[-1].copy()
    
    # X[0] and Y[1] location updates from offset Dictionary containing direction 

    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Collision checker
    if new_head in snake or new_head[0] < -WIDTH/2 or new_head[0] > WIDTH/2\
        or new_head[1] < -HEIGHT/2 or new_head[1] > HEIGHT/2:
        
        if tryagain():
            reset()
        else:
            turtle.bye()
    else:
        snake.append(new_head)

        # If snake doesn't eat it stays the same length
        if not eat_food(): 
            snake.pop(0)
        else: levels()

    

        if SCORE >= 1:
            canvas.title(f'Snake         Score: {SCORE}')
            


        for location in snake:
            my_turtle.goto(location[0], location[1])
            my_turtle.stamp()
        
        
        canvas.update()
        turtle.ontimer(game_loop, DELAY)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    '''Distance between 2 points using Pythagorean Theorem'''
    distance = math.sqrt(math.pow((y2-y1), 2) + math.pow((x2-x1), 2))
    return distance

def generate_food_location():
    '''Same as border collision but with offset to avoid putting food outside
        the game frame
    '''
    x = random.randint(-WIDTH/2 + FOOD_SIZE, WIDTH/2 - FOOD_SIZE)
    y = random.randint(-HEIGHT/2 + FOOD_SIZE, HEIGHT/2 - FOOD_SIZE)
    return x,y

def eat_food():
    global food_pos, SCORE
    if get_distance(snake[-1], food_pos) < 20:
        SCORE += 1
        food_pos = generate_food_location()
        food.goto(food_pos)

        return True
    return False

def food_mixer():
    '''Store food shapes in dict, whenever snake eats generate new food shape
        and color'''
    pass

def tryagain():
    # Displays Score when user dies
    response = tkinter.messagebox.askyesnocancel(title="GAME OVER", message=f'Oops you died Your score is {SCORE}\
        \nWant another shot?')
    return response




###Canvas
canvas = turtle.Screen()
# canvas.bgpic('./')
canvas.title(f'Welcome to Snake')
canvas.setup(WIDTH, HEIGHT)
canvas.title("Snake")
canvas.bgcolor('Black')
canvas.tracer(0)
#####

# Event Handler
canvas.listen()
direction_keys()


# ////Turtle Object Description
my_turtle = turtle.Turtle()
my_turtle.shape("square")
my_turtle.color("white", "green")
my_turtle.penup()
my_turtle.stamp()

# Food Turtle Item
food = turtle.Turtle()
food.shape("circle")
food.shapesize(FOOD_SIZE/20) #In Pixel
food.color("Black", "Yellow")
food.penup()






# Move Snake Along X-Axis
reset()

# Infinite loop to keep canvas open until 
# user presses X
turtle.done()





'''
Upcoming Features

Level Ups
- Add images for the food icons
- Add canvas backgroung image
- As level increases increase snake speed and change background designs
start with calm mode then add different effects
-Change snake design as it grows to a certain size 
- Food stays in one location for n seconds then disappears


Lost in the multiverse Mode 

-Use Different DS to add cool features and modes
- Invert Snake key bindings and make a multidimension snake game, 
mirror snake reflection and add effects.
- Add obstacles that come and go as level increases




- Utilize OOP and Separate Concerns
- Implement Dry 

'''
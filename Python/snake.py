"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

5.
"""

from turtle import *
from random import randrange
from freegames import square, vector

colors = ['cyan', 'dark goldenrod', 'chartreuse', 'purple', 'chocolate']
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
boundary = randrange(300, 500) #Randomizes board size

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -boundary < head.x < boundary and -boundary < head.y < boundary

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 10, colors[snakecolor])

    square(food.x, food.y, 6, colors[foodcolor])
    update()
    ontimer(move, 50) #Makes the game faster
    
setup(boundary*2, boundary*2, 370, 0)

snakecolor = randrange(0, 5)
foodcolor = snakecolor
while(foodcolor==snakecolor):
    foodcolor = randrange(0, 5)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

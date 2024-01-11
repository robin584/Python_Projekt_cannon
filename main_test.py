from random import randrange
from turtle import *
from vector_function import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


# Create cannon components
cannon = Turtle()
cannon.shape("square")
cannon.shapesize(1, 5)
cannon.color("black")
cannon.up()

ground = Turtle()
ground.shape("circle")
ground.shapesize(2)
ground.color("black")
ground.up()

arrow = Turtle()
arrow.shape("arrow")
arrow.shapesize(1)
arrow.color("red")
arrow.up()



def tap(x, y):

    cannon.goto(-195, -195)
    cannon.setheading(cannon.towards(x,y))
    
    ground.goto(-195, -195)
    ground.setheading(ground.towards(x,y))

    arrow.goto(-195, -195)
    arrow.setheading(arrow.towards(x,y))

    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """Draw ball, targets, and cannon."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

    # Update cannon position based on the mouse cursor

   

def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 10)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

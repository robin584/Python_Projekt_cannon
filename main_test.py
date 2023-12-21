from random import randrange
from turtle import *
from vector_function import vector

ball = vector(-200, -200)
speed = vector(0, 0)
objects = []  # Renamed from 'targets' to 'objects'
score = 0

def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """Draw ball and objects."""
    clear()

    for obj in objects:
        goto(obj.x, obj.y)
        if obj.is_green:
            draw_rectangle(20, 20, 'green')  # Draw green square
        else:
            dot(20, 'blue')  # Draw blue dot

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')  # Draw red ball

    # Display the score
    goto(-190, 190)
    write(f"Score: {score}", align="left", font=("Courier", 16, "normal"))

    update()

def draw_rectangle(width, height, color):
    """Draw a rectangle at the current turtle position."""
    fillcolor(color)
    begin_fill()
    for _ in range(4):
        forward(width if _ % 2 == 0 else height)
        right(90)
    end_fill()

def move():
    """Move ball and objects."""
    global score

    if randrange(40) == 0:
        y = randrange(-150, 150)
        obj = vector(200, y)
        obj.is_green = randrange(2) == 1  # Randomly set green target
        objects.append(obj)

    for obj in objects:
        obj.x -= 0.5

        # Check if the ball hits an object
        if inside(ball) and abs(obj - ball) <= 13:
            if obj.is_green:
                score += 2  # Score 2 points for hitting a green target
            else:
                objects.remove(obj)
                score += 1

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = objects.copy()
    objects.clear()

    for obj in dupe:
        if abs(obj - ball) > 13:
            objects.append(obj)

    draw()

    for obj in objects:
        if not inside(obj):
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()


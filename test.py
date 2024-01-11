from random import randrange
from turtle import *
from vector_function import vector  

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
score = 0  # Starting with a score of 0
lives = 3  # Starting with 3 lives
game_over = False

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
    global game_over
    # Let the whole cannon follow the screen tab
    cannon.goto(-195, -195)
    cannon.setheading(cannon.towards(x,y))
    
    ground.goto(-195, -195)
    ground.setheading(ground.towards(x,y))

    arrow.goto(-195, -195)
    arrow.setheading(arrow.towards(x,y))

    # Respond to screen tap
    if game_over:
        restart_game()
    elif not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    # Return True if xy within screen
    return -200 < xy.x < 200 and -200 < xy.y < 200


def restart_game():
    global score, game_over, lives
    score = 0
    lives = 3
    game_over = False
    targets.clear()
    move()


def draw_game_over():
    global lives
    goto(0, 0)
    write("GAME OVER", align="center", font=("Courier", 28, "normal"))
    goto(0, -30)
    write(f"Your Score: {score}", align="center", font=("Courier", 16, "normal"))
    goto(0, -60)
    write("Click to Restart", align="center", font=("Courier", 16, "normal"))
    lives = 0


def draw():
    global game_over
    clear()

    # Draw ball and targets
    for target in targets:
        goto(target.x, target.y)
        dot(20, target.color)

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    goto(-200, 185)
    write(f"Score: {score} | Lives: {lives}", align="left", font=("Arial", 16, "normal"))

    # If the lives go to 0 the GAME OVER screen appears
    if lives <= 0:
        game_over = True
        draw_game_over()
    update()


def move():
    global lives, score, game_over

    if randrange(40) == 0:
        y = randrange(-150, 150)
        color = 'blue'
        if randrange(10) == 0:  # 1 in 10 chance for a yellow target
            color = 'yellow'
        elif randrange(5) == 0:  # 1 in 5 chance for a black target
            color = 'black'

        target = vector(200, y, color=color)
        targets.append(target)

    for target in targets:
        target.x -= randrange(1, 2)  # Vary gravitational effect by adjusting the speed

    if inside(ball):
        speed.y += 0.30
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        elif target.color == 'yellow':  # Hitting a yellow target grants an extra life
            lives += 1
            score += 1  # Increment score when hitting a yellow target
        elif target.color == 'black':  # Hitting a black target results in losing a life
            lives -= 1
        else:
            score += 1  # Increment score when any other target disappears

    # Losing a life when the target hits the left wall
    for target in targets:
        if not inside(target):
            game_over = True
            if target.color != 'yellow':
                lives -= 1

    draw()
    ontimer(move, 20)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
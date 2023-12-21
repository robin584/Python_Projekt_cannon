from random import randrange
from turtle import *
from vector_function import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
score = 0
game_over = False

def draw_rectangle(width, height, color):
    """Draw a rectangle at the current turtle position."""
    fillcolor(color)
    begin_fill()
    for _ in range(4):
        forward(width if _ % 2 == 0 else height)
        right(90)
    end_fill()


def tap(x, y):
    global game_over
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
    global score, game_over
    score = 0
    game_over = False
    targets.clear()
    move()

def draw_game_over():
    goto(0, 0)
    write("GAME OVER", align="center", font=("Courier", 28, "normal"))
    goto(0, -30)
    write(f"Your Score: {score}", align="center", font=("Courier", 16, "normal"))
    goto(0, -60)
    write("Click to Restart", align="center", font=("Courier", 16, "normal"))

def draw():
    # Draw ball and targets
    clear()

    for i, target in enumerate(targets):
        goto(target.x, target.y)
        if i % 2 == 0:
            draw_rectangle(20, 20, 'green')  # Draw green square
        else:
            dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    # Display the score
    goto(-190, 190)
    write(f"Score: {score}", align="left", font=("Courier", 16, "normal"))

    if game_over:
        draw_game_over()

    update()

def move():
    global score, game_over

    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

        # Check if the ball hits a target
        if inside(ball) and abs(target - ball) <= 13:
            targets.remove(target)
            score += 1

        update()

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
            game_over = True
            draw()

    ontimer(move, 20)

def main():
    setup(420, 420, 370, 0)
    hideturtle()
    up()
    tracer(False)
    onscreenclick(tap)
    move()
    done()

if __name__ == "__main__":
    main()

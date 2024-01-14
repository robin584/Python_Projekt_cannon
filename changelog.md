# Changelog of the Cannon Project

**Hint:** The "..." indicates the places in the documentation where non-important code is omitted to save space.

## Change 1
- Varied gravitational effect:
  ```python
  if inside(ball):
      speed.y -= 0.30     # Invert the gravitation effect by adding a "-"
      ball.move(speed)


## Change 2
- I adjusted the speed of the red ball:
  ```python
  draw()
    ontimer(move, 20)   # you can change the speed from 1 (very fast) to 50 (very slow)


## Change 3
- The third change was the implemented score board, which encreases if a target gets hit:
  ```python
  # prints the score on the screen
  score = 0  # Starting with a score of 0
  ...
  goto(-200, 185)
    write(f"Score: {score} | Lives: {lives}", align="left", font=("Arial", 16, "normal"))
  ...
  for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
                score += 1  # Increment score when any other target disappears


## Change 4
- I have implemented a life counter. You start with 3 lives every time you play the game:
  ```python
  lives = 3  # Starting with 3 lives
  ...
  goto(-200, 185)
    write(f"Score: {score} | Lives: {lives}", align="left", font=("Arial", 16, "normal"))


## Change 5
- When a target hits the left barrier of the screen, you lose a life:
  ```python
  # Losing a life when the target hits the left wall
    for target in targets:
        if not inside(target):
          lives -= 1


## Change 6
- The 6. thing I have changed was the new GAME OVER screen if you lost every life:
  ```python 
  game_over = False   # I set up a variable called game over with a value of False
  ...
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

  ...
  def restart_game():   # Function that is executed when you restart the game
    global score, game_over, lives
    score = 0
    lives = 3
    game_over = False
    targets.clear()
    move()

  ...
  def draw_game_over():  # Visualize the GAME OVER screen
    global lives
    goto(0, 0)
    write("GAME OVER", align="center", font=("Courier", 28, "normal"))
    goto(0, -30)
    write(f"Your Score: {score}", align="center", font=("Courier", 16, "normal"))
    goto(0, -60)
    write("Click to Restart", align="center", font=("Courier", 16, "normal"))
    lives = 0

    ...
    def draw():
    global game_over
    clear()
    ...
    # If the lives go to 0 the GAME OVER screen appears
    if lives <= 0:
        game_over = True    # If the lives go to 0, then the game_over variable change the value to "True"
        draw_game_over()    # Brings up the game over screen
    update()

    ...
    def move():
    global lives, score, game_over
    ...
    # Losing a life when the target hits the left wall
    for target in targets:
        if not inside(target):
            game_over = True
            lives -= 1
    
## Change 7
- I created a new target that is black (it spawns in 1 out of 5 cases). If this target is hit then you lose a life:
  ```python
  def move():
    global lives, score, game_over

    if randrange(40) == 0:
        y = randrange(-150, 150)
        color = 'blue'
        if randrange(5) == 0:  # 1 in 5 chance for a black target
            color = 'black'

        target = vector(200, y, color=color)
        targets.append(target)
  ...
  for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        elif target.color == 'black':  # Hitting a black target results in losing a life
            lives -= 1
        else:
            score += 1  # Increment score when any other target disappears

    # Losing a life when the target hits the left wall
    for target in targets:
        if not inside(target):
            game_over = True
            if target.color != 'black':   # The black target can go out of the screen without losing a life
              lives -= 1
 
## Change 8
- I also created a yellow target (it spawns in 1 out of 10 cases). If this target is hit, then you gain a life:
  ```Python
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
    ...
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


## Change 9
- Finally, I used the turtle function to create geometric shapes to visualize a cannon in the bottom left corner (from which the red ball comes). The cannon follows the mouse cursor when you click on the screen to trigger the red ball.
  ```python
  # Create cannon components
  cannon = Turtle()    # Links the Turtle function
  cannon.shape("square")   # "shape" generates the geometric form
  cannon.shapesize(1, 5)  # "shapesize" sets the size of the object
  cannon.color("black")  # "color" sets the color for the object
  cannon.up()  # no line is drawn where the cannon shows

  # Ground creates the bottom of the cannon
  ground = Turtle()
  ground.shape("circle")
  ground.shapesize(2)
  ground.color("black")
  ground.up()

  # Arrow shows the direction of the cannon
  arrow = Turtle()
  arrow.shape("arrow")
  arrow.shapesize(1)
  arrow.color("red")
  arrow.up()

  ...
  def tap(x, y):
    global game_over
    # Let the whole cannon follow the screen tab
    cannon.goto(-195, -195)  # Sets the position for the cannon
    cannon.setheading(cannon.towards(x,y))
    
    ground.goto(-195, -195)
    ground.setheading(ground.towards(x,y))

    arrow.goto(-195, -195)
    arrow.setheading(arrow.towards(x,y))



### Additional Bug Fixes (that can be done) (but i had no time for)
- At the beginning the cannon floats in the center of the screen and only goes to its target position (goto(-195, -195)) when you click on the screen once.
- A bug occurs when a target touches the left wall. Because sometimes you lose 4 lives with a target. But in the GAME OVER screen every target only deducts one life.


### Conclusion:
It was a very exciting project that I really enjoyed. Because of the challenges, I learned a lot of new things. The most difficult change in my opinion was the implementation of the Game Over screen with all its calls and functions. Nevertheless, after a long time of debugging, I finished it.
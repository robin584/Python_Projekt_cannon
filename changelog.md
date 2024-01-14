# Changelog of the Cannon Project


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
 
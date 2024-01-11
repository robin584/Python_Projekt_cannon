from turtle import *

def follow_mouse(x, y):
    turtle.setheading(turtle.towards(x, y))
    turtle.goto(x, y)

# Initialisiere das Turtle-Fenster
setup(500, 500)
title("Mauszeiger verfolgen")

# Erstelle ein Turtle-Objekt
turtle = Turtle()
turtle.shape("turtle")
turtle.speed(2)

# Reagiere auf Mausklicks
onscreenclick(follow_mouse)

# Hauptschleife starten
done()

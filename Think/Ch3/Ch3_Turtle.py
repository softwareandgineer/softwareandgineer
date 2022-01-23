import turtle

import random

window = turtle.Screen()

window.bgcolor("black")

alex = turtle.Turtle()

alex.color("white")

angle = random.randint(0,360)

while(True):
    angle = random.randint(0,360)
    alex.right(angle)
    alex.forward(25)

window.mainloop()

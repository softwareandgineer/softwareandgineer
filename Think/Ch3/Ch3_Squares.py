import turtle

window = turtle.Screen()

window.bgcolor("black")

alex = turtle.Turtle()

alex.color("white")


def draw_square(t, width):
    for _ in range(4):
        alex.forward(width)
        alex.right(90)


width = 20
for i in range(30):
    width = width + 5
    alex.right(10)
    draw_square(alex, width)



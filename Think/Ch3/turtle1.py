import turtle


def fractal(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        fractal(t, order - 1, size / 3)
        t.left(60)
        fractal(t, order - 1, size / 3)
        t.right(120)
        fractal(t, order - 1, size / 3)
        t.left(60)
        fractal(t, order - 1, size / 3)


window = turtle.Screen()

window.title("turtle")

alex = turtle.Turtle()

fractal(alex, 5, 2000)
window.mainloop()

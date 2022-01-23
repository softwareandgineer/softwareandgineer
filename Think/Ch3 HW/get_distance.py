def distance(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    d = (x * x + y * y) ** 0.5
    return d

print(distance(0, 3, 4, 0))

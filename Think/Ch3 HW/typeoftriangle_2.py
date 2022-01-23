x = float(input("Give me the first length"))
y = float(input("Give me the second length"))
z = float(input("Give me the third length"))
threshold = 1e-7
def is_right_angle(x, y, z):
    if abs( x ** 2 + y ** 2 - z ** 2) < threshold:
        return True
    else:
        return False

print(is_right_angle(x,y,z))








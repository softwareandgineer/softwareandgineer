h = float(input("Give me the hypotenuse"))
L2 = float(input("Give me the second length"))
L3 = float(input("Give me the third length"))

def pytha(h, L2, L3):
    if L2**2 + L3**2 == h:
        return True
    else:
        return False


print(pytha(h,L2,L3))
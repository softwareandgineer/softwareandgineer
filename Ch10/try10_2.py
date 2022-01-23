n1 = int(input("Gimme first num:"))
n2 = int(input("Gimme second num:"))

try:
    n = n1 // n2
    r = n1 % n2
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print(f"{n1} / {n2} = {n}")
    print("Your remainder is " + str(r))

a3 = int(input())
a2 = int(input())
a1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())

at = a3 * 3 + a2 * 2 + a1
bt = b3 * 3 + b2 * 2 + b1

if at > bt:
    print("A")
elif bt > at:
    print("B")
else:
    print("T")


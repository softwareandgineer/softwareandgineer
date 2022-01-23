import math
x = 4.0

while(math.fabs(x * x - 2.0) > 0.00001):
    x = x - (x*x - 2.0) / (2 * x)

print(x)


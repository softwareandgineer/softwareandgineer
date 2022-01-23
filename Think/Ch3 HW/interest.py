P = float(input("Principal Amount"))
r = float(input("Interest rate as decimal"))
n = float(input("Number of times interest is compounded per year"))
t = float(input("Total number of years"))

def interest(P, r, n, t):
    A = P * (1 + r/n) ** (n*t)
    return A

print(interest(P, r, n, t))
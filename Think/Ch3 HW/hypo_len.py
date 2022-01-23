L1 = int(input("Give me the first length"))
L2 = int(input("Give me the second length"))

def hypo(L1, L2):
    m = L1**2 + L2**2
    print(m ** 0.5)


print(hypo(L1,L2))

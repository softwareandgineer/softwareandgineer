def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True


for i in range(10000):
    if is_prime(i):
        print(i)

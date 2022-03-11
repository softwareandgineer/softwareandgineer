x = int(input())
m = int(input())
result = 0

for n in range(1, m+1):
    if x * n % m == 1:
        result = n
        break


if result == 0:
    print("No such integer exists.")
else:
    print(result)


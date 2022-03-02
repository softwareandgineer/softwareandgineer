def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


lst = [fib(n) for n in range(10)]
print(lst)


def factorial(i):
    if i == 0:
        return 1
    else:
        return i * factorial(i - 1)


print(factorial(5))


def nested_sum(l):
    total = 0
    for element in l:
        if type(element) is list:
            total += nested_sum(element)
        else:
            total += element

    return total


v = [10, 20, [30, [70, 80], 40], 50]

result = nested_sum(v)
print(result)


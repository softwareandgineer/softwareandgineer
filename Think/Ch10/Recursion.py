def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


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


def nested_max(l):
    m = None
    for element in l:
        if type(element) is list:
            x = nested_max(element)
        else:
            x = element
        if m is None or x > m:
            m = x

    return m


print(nested_max(v))


def nested_depth(ls):
    d = None
    for element in ls:
        if type(element) is list:
            current_depth = 1 + nested_depth(element)
        else:
            current_depth = 1
        if d is None or d < current_depth:
            d = current_depth
    return d

print(nested_depth(v))

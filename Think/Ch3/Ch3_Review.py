import sys

#if else

def my_min(a, b):
    if a < b:
        return a
    else:
        return b

print(my_min(3242,4544))

#for loops

def my_list_min(list):
    m = list[0]
    for i in list[1:]:
        if i < m:
            i = m
        else:
            continue
    return m

#sys.maxsize finds greatest value for 'm'

def my_list_min_conv(list):
    m = sys.maxsize
    for i in list:
        if i < m:
            m = 1
    return m

list = [1,2]
print(my_list_min(list))

#calculations

def factorial(n):
    m = 1
    for i in range(1, n+1):
        m = m*(i)
    return m

print(factorial(5))

#binary to number conversion
#while loop

def to_binary(n):
    list = []

    while n > 0:
        r = n % 2
        list.append(r)
        n = n // 2

    list.reverse()
    return list

print(to_binary(16123849))





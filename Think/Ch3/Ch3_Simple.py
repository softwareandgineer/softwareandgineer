def sum_list(l):
    n = 0
    for i in l:
        n = n + i
    return n


def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False


def count_digits(n):
    digits = 0
    while (n != 0):
        digits = digits + 1
        n = n // 10

    return digits


def power_table():
    for i in range(0, 12):
        n = i ** 2
        print(str(i) + "\t" + str(n))


def count_pos(lst):
    n = 0
    for i in lst:
        if i > 0:
            n += 1
    return n


def get_dist_to_edge(width, i):
    return n


def print_square(width):
    for i in range(0, width):
        n = get_dist_to_edge(width, i)
        line = ""
        for j in range(0, width):
            line += "\t" + str(n)
        print(line)


lit = [1, 2, 3, 4]
print(sum_list(lit))

n = 35
print(is_odd(35))

print(count_digits(12331))

power_table()

lst = [0, -5, -6, 2, 123, -123, 1, 2, -2, -5]
n = count_pos(lst)
print(n)

print_square(5)

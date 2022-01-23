def find_min (lst):
    m = lst[0]
    for i in lst[1:]:
        if i < m:
            m = i
    return m


lst = [2, 3, 7, 1, -23, 5]
m = find_min(lst)
print(m)


def has_odd(lst):
    for i in lst:
        if i % 2 == 1:
            return False
    return True


lst = [2, 4, 6, 8]
x = has_odd(lst)
print(x)

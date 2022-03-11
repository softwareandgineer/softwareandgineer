def get_digits(n):  # turns input into list
    lst = []

    while n > 0:  # separates number into digits
        r = n % 10
        lst.append(r)
        n = n // 10

    lst.reverse()  # returns list to original because numbers are inserted backwards (can also use lst.insert)
    return lst


def is_rotatable(lst):
    i = 0
    j = len(lst) - 1

    still_good = True
    while i <= j:
        if lst[i] == lst[j] == 0 or lst[i] == lst[j] == 1 or lst[i] == lst[j] == 8 or (lst[i] == 6 and lst[j] == 9) or (
                lst[i] == 9 and lst[j] == 6):
            i += 1
            j -= 1
        else:
            still_good = False
            break

    return still_good


count = 0
n = int(input())
m = int(input())
for i in range(n, m + 1):
    if is_rotatable(get_digits(i)):
        count += 1

print(count)

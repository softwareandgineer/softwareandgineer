lst = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]


def get_num():
    while True:
        n = int(input("Give me a number from 0-6"))
        if n > 6 or n < 0:
            print("You cannot choose this number")
            continue
        return n

def get_len():
    l = int(input("How long will you be staying"))
    return l


n = get_num()
l = get_len()

result = ((n + l) % 7)
print(lst[result])









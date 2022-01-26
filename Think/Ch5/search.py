str = "banana"
index = str.find("na")
print(index)

def my_find_first_letter (haystack, needle):
    for idx, letter in enumerate(haystack):
        if letter == needle:
            return idx
    return -1

index = my_find_first_letter("banana", "n")
print(index)

total_score = 0

def play():
    global total_score
    total_score = 100
    print(f"total_score = {total_score} inside function")


play()
print(f"total_score = {total_score} outside function")

#--------------------------------------------------------

long_str = "i love c++"
lst = long_str.split()
print(lst)

#----------------------------------------
name1 = "Paris"
name2 = "Hilton"
name3 = "Whitney"
print("Pi is {0:.3f} {1:.4f}".format(333.141592, 1.2345))

print("{0:<15}{1:^15}{2:>15}".format(name1, name2, name3)) #left right center

#---------------------------------------------
layout = "{0:>4} {1:>6} {2:>6} {3:>6} {4:>13} {5:>24}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**2o"))
for i in range(1,11):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))


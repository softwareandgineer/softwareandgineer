numbers = [10, 20, 30, 40]
for n in numbers:
    print(n)

print(numbers[2:])  # starts from 2 in the list, be wary that lists start from 0

print(numbers[:-2])  # excludes the -2 in the list, if negative sign it starts from the opposite side and excludes
# the current number it is on

# how to change the numbers in the list, use the index
for i in range(len(numbers)):
    numbers[i] = -numbers[i]

print(numbers)

# boolean example, returns True or False
print(-10 in numbers)
print(-10 not in numbers)

# list operations: + (adds lists together) (append)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

# list operations: * (times) (repeats)
print([0] * 4)
list4 = list3 * 4
print(list4)

# deletes elements from list
del list1[0]
print(list1)

# is and is not

a = "banana"
b = "banana"

if a == b:
    print("a == b")
else:
    print("a != b")

# a and b point to the same thing from optimization

print(a is b)  # true

# however lists are changeable, so it is false

c = [1, 2, 3]
d = [1, 2, 3]
print(c is d)  # false

e = d
print(e is d)  # true

# you can make a real copy by using [:]

f = d[:]
print(f is d)  # False
f[2] = 300
print(f)
print(d)

# find all even numbers within 20, range loops

lst = []
for i in range(20 + 1):
    if i % 2 == 0:
        lst.append(i)
print(lst)

# list comprehension

lst = [n for n in range(21) if n % 2 == 0]  # add another n in the beginning for list comprehension
print(lst)

# -------------------------------------------------

# string and lists

# splitting words
line = "the rain in Spain..."
words = line.split()
print(words)

# splitting numbers
line = "1 2 3 4 5 6 7"
num_list = [int(n) for n in line.split()]
print(num_list)

# joining strings
lst = ["abc", "def", "ghl"]
s = "--".join(lst)
print(s)

# -------------------------------------------------

# matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(matrix)
matrix[1][1] = 50  # 1,1 is the coords, this changes the value
print(matrix)

for row in range(3):
    for col in range(3):
        matrix[row][col] *= 100

print(matrix)

#----------------------------------------------------
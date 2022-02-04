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
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)

# list operations: * (times) (repeats)
print([0] * 4)
list4 = list3 * 4
print(list4)

# deletes elements from list
del list1[0]
print(list1)




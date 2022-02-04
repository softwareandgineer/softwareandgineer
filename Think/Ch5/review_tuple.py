import math

# a tuple is a list with circle brackets, its inside values are immutable
year_born = ("Paris Hilton", 1981)
print(year_born[0])

# in order to add items, you must create a new tuple or list and add them together

another_year = (1999,)  # for single integer tuple, add a ", " for it to register
print(year_born + another_year)

# tuple packing
bob = ("Bob", 19, "CS")
print(bob)

# tuple unpacking
(name, age, studies) = bob
print(name)
print(age)
print(studies)


# use of tuple examples

def circle_stats(r):
    circumference = 2 * math.pi * r
    area = math.pi * r * r
    return circumference, area


(l, a) = circle_stats(100.0)
print(f"circumference is {l}, area is {a}")

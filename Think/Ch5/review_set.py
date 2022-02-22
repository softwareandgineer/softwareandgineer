# sets are unordered and mutable containers
# sets are for fast access (fast searching) faster than lists
# uses hash functions for searching (one of the most useful techniques in CS)

my_set = {1, 2, 3, 4}
print(my_set)

my_set2 = {3, 4, 5, 6}
print(my_set2)

my_set.add(5)  # adds a value
print(my_set)

# set operations: unions, differences, intersections
set_3 = my_set | my_set2  # union
print(set_3)

set_4 = my_set - my_set2  # difference
print(set_4)

set_5 = my_set & my_set2  # intersection
print(set_5)

# frozenset : immutable sets'
fz_set = frozenset([1,2,3])
print(fz_set)
# e.g. you cannot do fz_set.add because it is immutable

# -----------------------------------------------------------
#                       Ordered                Unordered
# Mutable                list                   set, dict
# Immutable              tuple                  frozenset
# -----------------------------------------------------------


# two methods of creating a dictionary

english_french: dict[str, str] = {}

english_french["one"] = "un(e)"
english_french["two"] = "deux(se)"

print(english_french)

english_french2 = {
    "one": "un(e)",
    "two": "deux(se)"
}

print(english_french2)

# operations
inventory = {"apples": 430, "bananas": 312, "oranges": 525}
print(inventory)
del inventory["bananas"]  # deletes an item from the dictionary, works in lists too
print(inventory)

inventory["apples"] += 100  # changes values
print(inventory)

print(len(inventory))  # displays the amount of items in the dict or list

# dictionary methods
for i in english_french.keys():  # prints out all specific items
    print(i)

for y in english_french.values():  # prints out the each item's associated value
    print(y)

for x in english_french.items():  # prints the key and value together in tuple format
    print(x)

# convert keys/values/items to a list
my_keys = list(english_french.keys())
print(my_keys)

# loops
for (key, value) in inventory.items():
    print(f"we have {value} {key}")

# use "in" to test if a key exists in a dictionary
if "bananas" in inventory:
    print("we have bananas")
else:
    print("we don't have bananas")

# alias and copy
# alias
another_inventory = inventory  # creating the alias
print(another_inventory)
print(inventory)
another_inventory["apples"] += 1000  # they both refer to the same thing so both their "apple" values add 1000
print(another_inventory)
print(inventory)

# copy
another_inventory2 = inventory.copy()  # creating a copy of the inventory
another_inventory2["apples"] += 1000 
print(another_inventory2)
print(inventory)  # no changes because it is identical with a copy and not the actual inventory





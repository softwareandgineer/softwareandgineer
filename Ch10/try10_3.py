filename = "abc.txt"
try:
    with open(filename) as file:
        content = file.read()
except FileNotFoundError:
    print(F"{filename} does not exist")
else:
    print(content)

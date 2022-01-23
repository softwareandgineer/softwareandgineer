filename = input("Give me the file name:")

try:
    with open(filename) as file:
        content = file.read()
        word_list = content.split()
        print(f"It has {len(word_list)} word(s)")
except FileNotFoundError:
    print(f"{filename} does not exist")
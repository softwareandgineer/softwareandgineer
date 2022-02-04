prefixes = "OQ"
suffix = "uack"

for letter in prefixes:
    print(letter + suffix)


# --------------------------------

def count_letters(word, x):
    count = 0
    for i in word:
        if i == x:
            count += 1
    return count


print(count_letters('banana', 'a'))


# ---------------------------------------------

def find_letters(wrd, x, loc=0):
    pos = -1
    start = -1
    while True:
        start = pos+1
        pos = wrd.find(x, start)
        if pos == -1:
            break

    if loc:
        loc = start

    return start


print(find_letters("cheeses", "s"))

#----------------------------------------------


def analyse_string(st):
    sct = 0
    for i in st:
        if i == " ":
            sct += 1
    return sct + 1
            

print(analyse_string('banana pp pp'))




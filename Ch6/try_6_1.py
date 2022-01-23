blackperson = {
        'color': 'green',
        'lives': 2,
        'name': 'neegro'
}

blackperson['lives'] -= 1

print(blackperson['name'] + 'has lives' + str(blackperson['lives']))

blackperson['speed'] = 9000

blackperson['vertical'] = 9999

print(blackperson)

for v in blackperson.values():
        print("value " + str(v))
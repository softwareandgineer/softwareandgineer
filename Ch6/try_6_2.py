zombies = []

walker = {'speed': 'medium',
         'health': 'medium',
          'size': 'standard'}

runner = {'speed': 'fast',
          'health': 'medium',
          'size': 'standard'}

crawler = {'speed': 'slow',
           'health': 'half',
           'size': 'small'}

brute = {'speed': 'medium',
         'health': 'high',
         'size': 'large',
         'attacks': {'regular': 1, 'laser': 0.5, 'explosives': 2}
}

zombies.append(walker)
zombies.append(runner)
zombies.append(crawler)
zombies.append(brute)

print(zombies)

age = input("Please input your age:")
age = int(age)
if age <= 18:
    print("You are too young to play")
    exit(0)
else:
    print("Okay, welcome to the Zombie Game")

choice = input("choose your zombie:");
print("You have chosen the " + choice)




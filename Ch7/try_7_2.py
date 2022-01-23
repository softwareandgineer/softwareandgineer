responses = []

quiz = True

while quiz:
    Name = input('What is your name?')
    Fav_S = input('Favourite colour?')
    responses.append({Name: Fav_S})
    repeat = input('Do you wish to continue? (Yes or No)')
    if repeat == 'Yes':
        quiz = True
    else:
        quiz = False
print(responses)









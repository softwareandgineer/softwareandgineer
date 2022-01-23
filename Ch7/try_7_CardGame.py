from random import randint

Comp_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
My_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

wins = 0

while Comp_cards:
    print("my card")
    print(My_cards)

    Comp_card_index = randint(0, len(Comp_cards)-1)
    Comp_card = Comp_cards[Comp_card_index]
    while True:
        Your_card = int(input("Pick your card:"))
        if Your_card not in My_cards:
            print("illegal move")
        else:
            break

    if Your_card > Comp_card:
        wins +=1
    print("computer choose:" + str(Comp_card))
    Comp_cards.remove(Comp_card)
    My_cards.remove(Your_card)

print("wins = " + str(wins))
if wins > 5:
    print("won")
elif wins < 5:
    print("lost")
elif wins == 5:
    print("tie")
#Welcome message and rules

print('\tWelcom to the text version of the DrinkingTri drinking game! \nEach player receives 4 cards, having to answer the followeing questions about them (each, once): \n\n-Card color (Red or Black); \n-Even or odd card; \n-Card suit; \n-Card with greater or lesser value than last. \n\n\tThen choose how many levels your triangle will have. Each level with one fewer card than the previous. So a 7-level triangle will start with 7 cards, then 6, and so forth. \n\tOn each level, cards are revealed in orther and an action is taken for people holing cards of same value. \n\tActions are, in turn, "have a drink" and "give a drink". The first card in every level is always "have a drink". \nE.G.: You are on level 2 (actions in double). First card is a 6. Player 1 has two 6, and player 1 has a single 6. That means Player 1 will have to drink 4 and player 1 hass to drink 2! (yes, repeated cards count). If this was o the second card, then Player one could giv out 4 drinks, as they please, and PLayer 2 gives out 2. If no one has the revealed card, another is drawn! \nThe game continues until the last floor, and, since it has only one card, the only action is to "Take a drink"! \nGood luck and Good Game')

print("\nNote: Distributed cards aren't removed from the deck so as not to limit the game to only the standard 52 card deck. That alse means more than 4 of a card could appear. However, the game was limited to 20 players and 20 levels on the Triangle")

#Deck creation, with an index; splitting in odd/even, color and suits

deck = ['AH', 'AD', 'AS', 'AC', '2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C', '4H', '4D', '4S', '4C', '5H', '5D', '5S', '5C', '6H', '6D', '6S', '6C', '7H', '7D', '7S', '7C', '8H', '8D', '8S', '8C', '9H', '9D', '9S', '9C', '10H', '10D', '10S', '10C', 'JH', 'JD', 'JS', 'JC', 'QH', 'QD', 'QS', 'QC', 'KH', 'KD', 'KS', 'KC']


cardValue = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13 ,13, 13, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13 ,13, 13]

even=['2H', '2D', '2S', '2C', '4H', '4D', '4S', '4C', '6H', '6D', '6S', '6C', '8H', '8D', '8S', '8C', '10H', '10D', '10S', '10C', 'QH', 'QD', 'QS', 'QC']

odd=['AH', 'AD', 'AS', 'AC', '3H', '3D', '3S', '3C', '5H', '5D', '5S', '5C', '7H', '7D', '7S', '7C', '9H', '9D', '9S', '9C', 'JH', 'JD', 'JS', 'JC', 'KH', 'KD', 'KS', 'KC']

black=['AS', 'AC', '2S', '2C', '3S', '3C', '4S', '4C', '5S', '5C', '6S', '6C', '7S', '7C', '8S', '8C', '9S', '9C', '10S', '10C', 'JS', 'JC', 'QS', 'QC', 'KS', 'KC']

red=['AH', 'AD', '2H', '2D', '3H', '3D', '4H', '4D', '5H', '5D', '6H', '6D', '7H', '7D', '8H', '8D', '9H', '9D', '10H', '10D', 'JH', 'JD', 'QH', 'QD', 'KH', 'KD']

hearts = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH']

diamonds = ['AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD']

spades = ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS']

clubs = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC']


import random

while True:
    playerNumber=input("\nHow many players are participating today?[Max. 20] ")
    if int(playerNumber) <= 20:
        break
    print("Invalid number. Exceeds player limit.")


playerHand = {}
players =[]


player = 1
while str(player) <= playerNumber:
    person=input("\nType in the name of player " + str(player) + ": ")
    players.append(person.title())
    player += 1

print("\nDone! So playing today we have: ")
for each in players:
    print(each.title())

#Dealing the cards to each player.
n = 1
for each in players:
    print(players[n-1].title() + "'s turn. To the questions:")
    hand = []
    color = input("\nWhat is your card's color?[R]ed or [B]lack ")
    draw1 = random.choice(deck)
    hand.append(cardValue[deck.index(draw1)])
    print(draw1)
    if color == "R".lower() and draw1 in red:
        print("Correct! Other players drink")
    elif color == "B".lower() and draw1 in black:
        print("Correct! Other players drink")
    else:
        print("Wrong! You take a drink.")

    oddEven = input("\nIs you card odd or even? [O]dd or [E]ven ")
    draw2 = random.choice(deck)
    hand.append(cardValue[deck.index(draw2)])
    print(draw2)
    if oddEven == "E".lower() and draw2 in even:
        print("Correct! Other players drink")
    elif color == "O".lower() and draw2 in odd:
        print("Correct! Other players drink")
    else:
        print("Wrong! You take a drink.")

    suit = input("\nWhat is the suit of your card? [H]earts, [D]iamonds, [C]lubs and [S]pades ")
    draw3 = random.choice(deck)
    hand.append(cardValue[deck.index(draw3)])
    print(draw3)
    if suit == "H".lower() and draw3 in hearts:
        print("Correct! Other players drink")
    elif suit == "D".lower() and draw3 in diamonds:
        print("Correct! Other players drink")
    elif suit == "S".lower() and draw3 in spades:
        print("Correct! Other players drink")
    elif suit == "C".lower() and draw3 in clubs:
        print("Correct! Other players drink")
    else:
        print("Wrong! You take a drink.")

    biggerSmaller = input("\nIs your card bigger or smaller than the last ( " + draw3 + ")? [+] bigger or [-] smaller ")
    draw4 = random.choice(deck)
    hand.append(cardValue[deck.index(draw4)])
    print(draw4)
    if biggerSmaller == "+" and cardValue[deck.index(draw4)] > cardValue[deck.index(draw3)]:
        print("Correct! Other players drink")
    elif biggerSmaller == "-" and cardValue[deck.index(draw4)] < cardValue[deck.index(draw3)]:
        print("Correct! Other players drink")
    else:
        print("Wrong! You take a drink.")

    playerHand[players[n-1]] = hand
    print(playerHand)
    n += 1

while True:
    levels = int(input("How many levels will the triangle have?[Max. 20] "))
    if int(levels) <= 20:
        break
    print("Invalid number. Exceeds game limit")

#Prints the triangle; Just a representation of how it would look like

for i in range(0, levels):
    for j in range(0, levels-i-1):
        print(end=" ")
    for j in range(0, i+1):
        print("X", end=" ")
    print()

print("There is your triangle! Let's go to the game rounds:")

input("Press 'Enter' to continue the game: ")

for n in range(0, levels):
    print("Level " + str(n+1) + " of " + str(levels))
    if(n == 0):
        input("Press 'Enter' to go into the first level ")
    else:
        input("Press 'Enter' to go into next level")
    for m in range(0, levels-n):
        print("Card " + str(m+1) + " of " + str(levels-n))
        input("Press 'Enter' to reveal next card ")
        i = False #setup boolean to restart loop in case a drawn card does't appear in anybody's hand
        while not i:
            carta = cardValue[deck.index(random.choice(deck))]
            print(carta)
            if str(carta) in str(playerHand.values()):
                for name, hand in playerHand.items():
                    if carta in hand:
                        cardCount = hand.count(carta)
                        if ((m+1) % 2) == 0:
                            print(name + " gives out " + str(cardCount * (m + 1)) + " drinks")
                        else:
                            print(name + " drinks " + str(cardCount * (m+1)))
                i = True
            else:
                input("No one had the card. Press 'Enter' to draw another.")

print("Congratulations! You all survived the game! Thank you for playing =D")
input("Press enter to end the program")
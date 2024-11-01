import itertools
import random

suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Card:
    def __init__(self, suit,  face):
        self.suit = suit
        self.face = face
    def __repr__(self):
        return f"{self.face} of {self.suit}"

deck = [Card(suit,face) for suit, face in itertools.product(suits, faces)]

def dealCard(card_deck_list, hand_list):
    hand_list.append(card_deck_list.pop(0))

def updateHandValue(hand, hand_value):
    num = 0
    for x in hand:
        card = hand[num]
        try:
            int(card.face)
        except ValueError:
            if card.face == "A":
                if hand_value + 11 > 21:
                    hand_value = hand_value + 1
                else:
                    hand_value = hand_value + 11
            else:
                hand_value = hand_value + 10
        else:
            hand_value = hand_value + int(card.face)
        finally:
            num = num + 1
    return hand_value

playerHand = []
dealerHand = []
playerHandValue = 0
dealerHandValue = 0

# Game logic
random.shuffle(deck)

dealCard(deck, playerHand)
dealCard(deck, playerHand)
dealCard(deck, dealerHand)
dealCard(deck, dealerHand)
playerHandValue = updateHandValue(playerHand, playerHandValue)
dealerHandValue = updateHandValue(dealerHand, dealerHandValue)
isDealerTurn = False

while isDealerTurn == False:
    print(f'''Your hand is:
    {playerHand}
    Score: {playerHandValue}
    ''')
    print(f'''The dealer shows:
    {dealerHand[1]}
    Score: {"not implemented yet im not gonna lie"}
    ''')

    if playerHandValue > 21:
        print(f"Bust! You automatically lose.")
        playerHandValue = 0
        isDealerTurn = True
    else:
        option_taken = input("""What do you want to do? You can:
        Hit
        Stand

        """)
        if option_taken == "Hit" or option_taken == "hit" or option_taken == "H" or option_taken == "h":
            dealCard(deck, playerHand)
            playerHandValue = updateHandValue(playerHand, playerHandValue)
        elif option_taken == "Stand" or option_taken == "stand" or option_taken == "S" or option_taken == "s":
            isDealerTurn = True
if isDealerTurn == True:
    print(f'''The dealer now shows:
    {dealerHand}
    Score: {dealerHandValue}
    ''')
    while dealerHandValue < 17:
        dealCard(deck, dealerHand)
        dealerHandValue = updateHandValue(dealerHand, dealerHandValue)
        print(f'''The dealer now shows:
        {dealerHand}
        Score: {dealerHandValue}
        ''')
if dealerHandValue == playerHandValue:
    print('Tie!')
elif dealerHandValue > playerHandValue:
    print('You Lose!')
else:
    print('You Win!')

import itertools
import random
import time
from tkinter import *

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
        card_value = getCardValue(card)
        if card_value == "A":
            if hand_value + 11 > 21:
                hand_value = hand_value + 1
                num = num + 1
            else:
                hand_value = hand_value + 11
                num = num + 1
        else:
            hand_value = hand_value + card_value
            num = num + 1
    return hand_value

def getCardValue(card):
    val = 0
    try:
        int(card.face)
    except ValueError:
        if card.face == "A":
            val = "A"
        else:
            val = 10
    else:
        val = int(card.face)
    return val

root = Tk()
root.title("Blackjack")
root.geometry("800x500")
root.resizable(False, False)
root.config(bg='#009900')


lb1 = Label(root, text="Player Hand", font=("Helvetica", 15), bg='#009900')
lb1.place(x=30, y=20)
lb2 = Label(root, text="Player Score", font=("Helvetica", 15), bg='#009900')
lb2.place(x=30, y=50)
lb3 = Label(root, text="Dealer Hand", font=("Helvetica", 15), bg='#009900')
lb3.place(x=30, y=110)
lb4 = Label(root, text="Dealer Score", font=("Helvetica", 15), bg='#009900')
lb4.place(x=30, y=140)

def gameLogic():
    playerHand = []
    dealerHand = []
    playerHandValue = 0
    dealerHandValue = 0

    random.shuffle(deck)

    dealCard(deck, playerHand)
    dealCard(deck, playerHand)
    dealCard(deck, dealerHand)
    dealCard(deck, dealerHand)
    playerHandValue = updateHandValue(playerHand, playerHandValue)
    dealerHandValue = updateHandValue(dealerHand, dealerHandValue)
    isDealerTurn = False

    while isDealerTurn == False:
        lb1.config(text=f"Player Cards: {playerHand}")
        lb2.config(text=f"Player Score: {playerHandValue}")
        lb3.config(text=f"Dealer Cards: {dealerHand[1]}")
        lb4.config(text=f"Dealer Score: {getCardValue(dealerHand[1])}")

        if playerHandValue > 21:
            print(f"Bust! You automatically lose.")
            lb1.config(text=f"Player Cards: {playerHand}")
            lb2.config(text=f"Player Score: {playerHandValue}")
            playerHandValue = -1
            time.sleep(1.5)
            isDealerTurn = True
        elif playerHandValue == 21:
            print(f"Blackjack!")
            lb1.config(text=f"Player Cards: {playerHand}")
            lb2.config(text=f"Player Score: {playerHandValue}")
            time.sleep(1)
            isDealerTurn = True
        else:
            option_taken = input('''What do you want to do? You can:
            Hit
            Stand

            ''')
            if option_taken == "Hit" or option_taken == "hit" or option_taken == "H" or option_taken == "h":
                dealCard(deck, playerHand)
                playerHandValue = 0
                playerHandValue = updateHandValue(playerHand, playerHandValue)
                lb1.config(text=f"Player Cards: {playerHand}")
                lb2.config(text=f"Player Score: {playerHandValue}")
            elif option_taken == "Stand" or option_taken == "stand" or option_taken == "S" or option_taken == "s":
                isDealerTurn = True
    if isDealerTurn == True:
        lb3.config(text=f"Dealer Cards: {dealerHand}")
        lb4.config(text=f"Dealer Score: {dealerHandValue}")
        while dealerHandValue < 17:
            dealCard(deck, dealerHand)
            dealerHandValue = 0
            dealerHandValue = updateHandValue(dealerHand, dealerHandValue)
            time.sleep(1)
            lb3.config(text=f"Dealer Cards: {dealerHand}")
            lb4.config(text=f"Dealer Score: {dealerHandValue}")
        if dealerHandValue > 21:
            dealerHandValue = -1
            isDealerTurn = False
    print('Your score is:', playerHandValue)
    print('The dealer\'s score is:', dealerHandValue)
    if dealerHandValue == playerHandValue:
        print('Tie!')
    elif dealerHandValue > playerHandValue:
        print('You Lose!')
    else:
        print('You Win!')
    playAgain = input('''Would you like to play again?
Yes/no (default answer is Yes, any other text entered will close the game): ''')
    if playAgain == "" or playAgain == "y" or playAgain == "Y" or playAgain == "Yes" or playAgain == "yes":
        gameLogic()

btn = Button(root, text="Play Round", font=("Helvetica", 15), bd=5, bg='#8B8386', fg='White', command=gameLogic)
btn.place(x=115, y=200)

root.mainloop()
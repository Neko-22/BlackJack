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
            else:
                hand_value = hand_value + 11
        else:
            hand_value = hand_value + card_value
        num += 1
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
root.geometry("650x400")
#root.resizable(False, False)
root.config(bg='#63B76C')


lb1 = Label(root, text="Player Cards:", font=("Source Code Pro", 15), bg='#63B76C')
lb1.place(x=10, y=20)
lb2 = Label(root, text="Player Score:", font=("Source Code Pro", 15), bg='#63B76C')
lb2.place(x=10, y=50)
lb3 = Label(root, text="Dealer Cards:", font=("Source Code Pro", 15), bg='#63B76C')
lb3.place(x=10, y=110)
lb4 = Label(root, text="Dealer Score:", font=("Source Code Pro", 15), bg='#63B76C')
lb4.place(x=10, y=140)
lb5 = Label(root, text="Let's have some fun!", font=("Source Code Pro", 15), bg='#63B76C')
lb5.place(x=10, y=170)

playerHand = []
dealerHand = []
playerHandValue = 0
dealerHandValue = 0

def checkPoints():
    global isDealerTurn
    global isPlayerTurn
    global playerHandValue
    if playerHandValue > 21:
        lb1.config(text=f"Player Cards: {playerHand}")
        lb2.config(text=f"Player Score: {playerHandValue}  BUST!")
        playerHandValue = -1
        dealerTurn()
    elif playerHandValue == 21:
        lb1.config(text=f"Player Cards: {playerHand}")
        lb2.config(text=f"Player Score: {playerHandValue}  BLACKJACK!")
        dealerTurn()

def hit():
    global playerHandValue
    dealCard(deck, playerHand)
    playerHandValue = 0
    playerHandValue = updateHandValue(playerHand, playerHandValue)
    lb1.config(text=f"Player Cards: {playerHand}")
    lb2.config(text=f"Player Score: {playerHandValue}")
    checkPoints()
    
def stand():
    dealerTurn()


def gameLogic():
    global playerHandValue
    global playerHand
    global dealerHand
    global dealerHandValue
    global isDealerTurn
    global isPlayerTurn
    global deck

    btn2.configure(state=NORMAL)
    btn3.configure(state=NORMAL)

    deck = [Card(suit,face) for suit, face in itertools.product(suits, faces)]
    random.shuffle(deck)

    playerHand = []
    dealerHand = []
    playerHandValue = 0
    dealerHandValue = 0

    dealCard(deck, playerHand)
    dealCard(deck, playerHand)
    dealCard(deck, dealerHand)
    dealCard(deck, dealerHand)
    playerHandValue = updateHandValue(playerHand, playerHandValue)
    dealerHandValue = updateHandValue(dealerHand, dealerHandValue)

    lb1.config(text=f"Player Cards: {playerHand}")
    lb2.config(text=f"Player Score: {playerHandValue}")
    lb3.config(text=f"Dealer Cards: {dealerHand[1]}")
    lb4.config(text=f"Dealer Score: {getCardValue(dealerHand[1])}")
    lb5.config(text=f"Let's have some fun!")

    checkPoints()

def endGame():
    if dealerHandValue == playerHandValue:
        lb5.config(text=f"It's a Tie!")
    elif dealerHandValue > playerHandValue:
        lb5.config(text=f"You lose! Sorry!")
    else:
        lb5.config(text=f"You win! Congratulations!")

def dealerTurn ():
    global dealerHand
    global dealerHandValue
    btn2.configure(state=DISABLED)
    btn3.configure(state=DISABLED)
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
        lb3.config(text=f"Dealer Cards: {dealerHand}")
        lb4.config(text=f"Dealer Score: {dealerHandValue} BUST!")
        dealerHandValue = -1
    endGame()

btn = Button(root, text="Play Round", font=("Source Code Pro", 15), bd=5, bg='#8B8386', fg='White', command=gameLogic)
btn.place(x=115, y=210)
btn2 = Button(root, text="Hit", font=("Source Code Pro", 15), bd=5, bg='#8B8386', fg='White', command=hit)
btn2.place(x=115, y=260)
btn3 = Button(root, text="Stand", font=("Source Code Pro", 15), bd=5, bg='#8B8386', fg='White', command=stand)
btn3.place(x=115, y=310)
root.mainloop()
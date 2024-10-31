import itertools

suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10]
faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Card:
    def __init__(self, suit, value, face):
        self.suit = suit
        self.value = value
        self.face = face
    def __repr__(self):
        return f"{self.face} of {self.suit}, value of {self.value}"

deck = [Card(suit,value,face) for suit, value, face in itertools.product(suits, values, faces)]
print(len(deck))
import random
from card import Card

class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [Card(suit, value) for suit in Deck.suits for value in Deck.values]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
    
    def check_for_reshuffle(self):
        if self.cards == 0:
            self.shuffle()
import random
from objects.card import Card


class Deck:
    def __init__(self):
        self.deck = [Card(value, suit) for value in range(2, 15) for suit in ['C', 'D', 'H', 'S']]
        random.shuffle(self.deck)

    def get_deck(self):
        return self.deck
    
    def deal(self):
        return self.deck.pop()

    def __str__(self):
        s = "[ "
        for card in self.deck:
            s += str(card) + ' '
        return s + ']'